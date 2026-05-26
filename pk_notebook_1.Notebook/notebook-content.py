# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "9b957c08-2fba-434a-94ae-1efaa59dc66a",
# META       "default_lakehouse_name": "pk_lh_2",
# META       "default_lakehouse_workspace_id": "320b1c27-3cbc-42ea-81b6-aba6ff5ec178",
# META       "known_lakehouses": [
# META         {
# META           "id": "9b957c08-2fba-434a-94ae-1efaa59dc66a"
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

df = spark.read.format("csv").option("header","true").load("Files/DATA/customers.csv")
# df now is a Spark DataFrame containing CSV data from "Files/DATA/customers.csv".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

notebookutils.session.stop()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
