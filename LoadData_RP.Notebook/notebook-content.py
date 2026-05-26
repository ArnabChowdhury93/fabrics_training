# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "f63a0cc6-b725-4baa-9f0b-0cf8ee4bd729",
# META       "default_lakehouse_name": "Revathi",
# META       "default_lakehouse_workspace_id": "320b1c27-3cbc-42ea-81b6-aba6ff5ec178",
# META       "known_lakehouses": [
# META         {
# META           "id": "f63a0cc6-b725-4baa-9f0b-0cf8ee4bd729"
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

df = spark.read.format("csv").option("header","true").load("Files/RawAdventureWorks_Customers.csv/AdventureWorks_Customers.csv")
# df now is a Spark DataFrame containing CSV data from "Files/RawAdventureWorks_Customers.csv/AdventureWorks_Customers.csv".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

notebookutils.session.stop

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
