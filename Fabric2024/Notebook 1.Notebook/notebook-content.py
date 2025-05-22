# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "4be21fb2-0ed3-4950-ade5-cf6aa7ea740e",
# META       "default_lakehouse_name": "lh_dp700",
# META       "default_lakehouse_workspace_id": "17d1bc90-2073-4fa5-9758-d4bb3dcd6a51",
# META       "known_lakehouses": [
# META         {
# META           "id": "4be21fb2-0ed3-4950-ade5-cf6aa7ea740e"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!

assignments = spark.sql("SELECT * FROM lh_dp700.dp700_e004.assignments")
departments = spark.sql("SELECT * FROM lh_dp700.dp700_e004.departments")
employees = spark.sql("SELECT * FROM lh_dp700.dp700_e004.employees")
projects = spark.sql("SELECT * FROM lh_dp700.dp700_e004.projects")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

assignments = spark.sql("SELECT * FROM lh_dp700.dp700_e004.assignments")
display(assignments)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

print(assignments)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

departments = spark.sql("SELECT * FROM lh_dp700.dp700_e004.departments")
employees = spark.sql("SELECT * FROM lh_dp700.dp700_e004.employees")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

display( \
    employees \
    .join(departments, employees["department_id"] == departments["department_id"], "left") \
    .select(
        employees["name"],
        employees["department_id"],
        departments["department_name"]
    ) \
)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
