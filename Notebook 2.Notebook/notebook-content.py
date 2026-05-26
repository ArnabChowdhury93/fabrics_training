# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "76bc0521-acc1-4457-a08f-7598da49f3a7",
# META       "default_lakehouse_name": "Day2_Lakehouse_1856",
# META       "default_lakehouse_workspace_id": "320b1c27-3cbc-42ea-81b6-aba6ff5ec178",
# META       "known_lakehouses": [
# META         {
# META           "id": "76bc0521-acc1-4457-a08f-7598da49f3a7"
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

import pandas as pd
# Load data into pandas DataFrame from "/lakehouse/default/Files/data_access/banking_lakehouse/customers.csv"
df = pd.read_csv("/lakehouse/default/Files/data_access/banking_lakehouse/customers.csv")
display(df)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
