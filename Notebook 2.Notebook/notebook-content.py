# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "1ec5c357-7b48-4598-ac0b-6aa586af7474",
# META       "default_lakehouse_name": "Arjun",
# META       "default_lakehouse_workspace_id": "33bc9708-5f6f-4292-a9da-d0b031f807eb",
# META       "known_lakehouses": [
# META         {
# META           "id": "1ec5c357-7b48-4598-ac0b-6aa586af7474"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

df = spark.read.format("csv").option("header","true").load("Files/Shortcut_TEST/RawAdventureWorks_Calendar/AdventureWorks_Calendar.csv")
# df now is a Spark DataFrame containing CSV data from "Files/Shortcut_TEST/RawAdventureWorks_Calendar/AdventureWorks_Calendar.csv".
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
