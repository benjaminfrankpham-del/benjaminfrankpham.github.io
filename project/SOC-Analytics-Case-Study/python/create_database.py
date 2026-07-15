import sqlite3
import pandas as pd

#loads the csv
df = pd.read_csv("data/soc_alerts.csv")

#connects the database
connection = sqlite3.connect("database/soc_alerts.db")

#dataframe to sql table
df.to_sql(
    "soc_alerts",
    connection,
    if_exists="replace",
    index=False
)

connection.close()

print("Database created successfully.")