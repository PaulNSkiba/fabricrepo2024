# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
print("Кластер запускается...")
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
print("✅ Spark активен. Версия:", spark.version)

import os
print("Spark environment:", os.environ.get("SPARK_HOME"))

from notebookutils import mssparkutils
try:
    from mssparkutils.credentials import getSecret
    print("✅ Модуль доступен")
except Exception as e:
    print("❌ Ошибка:", str(e))


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%pip install azure-eventhub
%pip install python-kucoin

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# INSTALL azure-eventhub before running!
# pip command:
# pip install azure-eventhub

from azure.eventhub import EventHubProducerClient, EventData
from kucoin.client import Client
from datetime import datetime, timezone
import hashlib
import random
import time
import json
from notebookutils import mssparkutils

vault_name = "https://kv-eventhub-streaming.vault.azure.net/"  # Пример: без протокола и домена
secret_hub = "eventhub-name"
secret_conn = "eventhub-connectionstr"

connection_str = mssparkutils.credentials.getSecret(vault_name, secret_conn)
hub_name = mssparkutils.credentials.getSecret(vault_name, secret_hub)

# Replace the placeholders with your Event Hubs connection string and event hub name
EVENTHUB_NAME = hub_name
CONNECTION_STR = connection_str
# Топ-10 криптовалютных пар
top_pairs = [
    'BTC-USDT', 'ETH-USDT', 'BNB-USDT', 'SOL-USDT', 'XRP-USDT',
    'ADA-USDT', 'DOGE-USDT', 'DOT-USDT', 'TRX-USDT', 'AVAX-USDT'
]
SLEEP_TIME = 3
client = Client(api_key='', api_secret='')

# Example message
'''
{
}
'''

# Create a producer client to send messages to the event hub
producer = EventHubProducerClient.from_connection_string(conn_str=CONNECTION_STR, eventhub_name=EVENTHUB_NAME)

def generate_event_id(payload):
    """Generate a SHA256 hash as a unique event ID."""
    hash_object = hashlib.sha256(json.dumps(payload, sort_keys=True).encode('utf-8'))
    return hash_object.hexdigest()

def get_current_timestamp():
    """Return the current timestamp in ISO 8601 format."""
    return datetime.now(timezone.utc)

# Ticker data for BTC-USDT: {'time': 1757942680062, 'sequence': '21999516845', 'price': '114884.5', 'size': '0.13547578', 'bestBid': '114888.4', 'bestBidSize': '0.90228029', 'bestAsk': '114888.5', 'bestAskSize': '0.50857347'}
# BTC-USDT: 114884.5

try:
    # Continuously generate and send fake temperature readings
    while True:
        # Create a batch.
        event_data_batch = producer.create_batch()
        current_timestamp = get_current_timestamp()
        for pair in top_pairs:
            try:
                ticker = client.get_ticker(pair)
                # print the ticker data to inspect its structure
                # print(f"Ticker data for {pair}: {ticker}")
                #price = ticker['price']
                print(f"{pair}: {ticker['price']}")
                # Create the payload
                payload = {
                    "source": 'KuCoin',
                    #"sequence": ticker['sequence'],
                    "pair": pair,
                    "price" : ticker['price'],
                    #"size": ticker['size'],
                    #"bestBid": ticker['bestBid'],
                    #"bestBidSize": ticker['bestBidSize'],
                    #"bestAsk": ticker['bestAsk'],
                    #"bestAskSize": ticker['bestAskSize'],
                    "origmsg": json.dumps(ticker),
                    "timestamp": current_timestamp.isoformat(),
                }
                            # Generate an event_id
                payload["event_id"] = generate_event_id(payload)
                date_column = current_timestamp.strftime("%Y%m%d")
                time_column = current_timestamp.strftime("%H:%M:%S")
                payload["date"] = date_column
                payload["time"] = time_column

                # Format the message as JSON
                message = json.dumps(payload)

                # Add the JSON-formatted message to the batch
                event_data_batch.add(EventData(message))
                
                # Send the batch of events to the event hub
                producer.send_batch(event_data_batch)
                
                # print(json.dumps(json.loads(message), indent=4))
                # print(event_data_batch)
            except Exception as e:
                print(f"Ошибка при получении {pair}: {e}")        
        

        
        # Wait for a bit before sending the next reading
        time.sleep(SLEEP_TIME)
except KeyboardInterrupt:
    print("Stopped by the user")
except Exception as e:
    print(f"Error: {e}")
finally:
    # Close the producer
    producer.close()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
