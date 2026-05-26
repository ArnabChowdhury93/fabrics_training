# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "d1bf05c2-03c5-485f-989a-f6cb9691222f",
# META       "default_lakehouse_name": "TavantRR",
# META       "default_lakehouse_workspace_id": "320b1c27-3cbc-42ea-81b6-aba6ff5ec178",
# META       "known_lakehouses": [
# META         {
# META           "id": "d1bf05c2-03c5-485f-989a-f6cb9691222f"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.read.format("csv").option("header","true").load("Files/input/banking_Data/accounts.csv")
# df now is a Spark DataFrame containing CSV data from "Files/input/banking_Data/accounts.csv".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
