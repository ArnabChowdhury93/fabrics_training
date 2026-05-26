-- Fabric notebook source

-- METADATA ********************

-- META {
-- META   "kernel_info": {
-- META     "name": "synapse_pyspark"
-- META   },
-- META   "dependencies": {
-- META     "lakehouse": {
-- META       "default_lakehouse": "2489387c-db49-4675-8ec6-bd78ab9caa28",
-- META       "default_lakehouse_name": "arnab_day3",
-- META       "default_lakehouse_workspace_id": "33bc9708-5f6f-4292-a9da-d0b031f807eb",
-- META       "known_lakehouses": [
-- META         {
-- META           "id": "e052730c-2795-4484-b4b5-3eb88b842814"
-- META         },
-- META         {
-- META           "id": "2489387c-db49-4675-8ec6-bd78ab9caa28"
-- META         }
-- META       ]
-- META     }
-- META   }
-- META }

-- CELL ********************

-- Welcome to your new notebook
-- Type here in the cell editor to add code!


-- METADATA ********************

-- META {
-- META   "language": "sparksql",
-- META   "language_group": "synapse_pyspark"
-- META }

-- CELL ********************

df = spark.read.format("csv").option("header","true").load("Files/input/market.csv")
# df now is a Spark DataFrame containing CSV data from "Files/input/market.csv".
display(df)

-- METADATA ********************

-- META {
-- META   "language": "sparksql",
-- META   "language_group": "synapse_pyspark"
-- META }
