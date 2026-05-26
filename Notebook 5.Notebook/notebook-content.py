# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "97b70fad-7752-4778-94ea-08faaa2afdb4",
# META       "default_lakehouse_name": "Tavant_lakehouse_1856",
# META       "default_lakehouse_workspace_id": "320b1c27-3cbc-42ea-81b6-aba6ff5ec178",
# META       "known_lakehouses": [
# META         {
# META           "id": "97b70fad-7752-4778-94ea-08faaa2afdb4"
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

df = spark.read.format("csv").option("header","true").load("Files/Raw@item().p_sink_folder/Raw{@item().p_sink_folder}/AdventureWorks_Calendar.csv")
# df now is a Spark DataFrame containing CSV data from "Files/Raw@item().p_sink_folder/Raw{@item().p_sink_folder}/AdventureWorks_Calendar.csv".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.read.format("csv").option("header","true").load("Files/Raw{@item().p_sink_folder}/AdventureWorks_Calendar.csv")
# df now is a Spark DataFrame containing CSV data from "Files/Raw{@item().p_sink_folder}/AdventureWorks_Calendar.csv".
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
