-- Fabric notebook source

-- METADATA ********************

-- META {
-- META   "kernel_info": {
-- META     "name": "synapse_pyspark"
-- META   },
-- META   "dependencies": {
-- META     "lakehouse": {
-- META       "default_lakehouse": "4be21fb2-0ed3-4950-ade5-cf6aa7ea740e",
-- META       "default_lakehouse_name": "lh_dp700",
-- META       "default_lakehouse_workspace_id": "17d1bc90-2073-4fa5-9758-d4bb3dcd6a51",
-- META       "known_lakehouses": [
-- META         {
-- META           "id": "4be21fb2-0ed3-4950-ade5-cf6aa7ea740e"
-- META         }
-- META       ]
-- META     }
-- META   }
-- META }

-- CELL ********************

-- Welcome to your new notebook
-- Type here in the cell editor to add code!
-- Create schema if not exists
CREATE SCHEMA IF NOT EXISTS dp700_e013;

-- Create the employees table
CREATE TABLE IF NOT EXISTS dp700_e013.employees (
    employee_id INT,
    name STRING,
    department_id INT,
    hire_date DATE,
    salary DECIMAL(10, 2)
);

INSERT INTO dp700_e013.employees VALUES
    (10, 'Lily Morgan', 104, '2024-12-10', 71000.00),
    (11, 'Noah Carter', 103, '2025-02-05', 69000.00);

-- METADATA ********************

-- META {
-- META   "language": "sparksql",
-- META   "language_group": "synapse_pyspark"
-- META }
