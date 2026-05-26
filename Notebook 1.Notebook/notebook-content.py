# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "b84af4c1-70e2-4a0a-ab3e-a4c55d89c81b",
# META       "default_lakehouse_name": "Sales_Lakehouse",
# META       "default_lakehouse_workspace_id": "33bc9708-5f6f-4292-a9da-d0b031f807eb",
# META       "known_lakehouses": [
# META         {
# META           "id": "b84af4c1-70e2-4a0a-ab3e-a4c55d89c81b"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

df = spark.read.csv(
    "Files/Sales_Data.csv",
    header=True,
    inferSchema=True
)

display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
