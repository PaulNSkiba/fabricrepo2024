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
