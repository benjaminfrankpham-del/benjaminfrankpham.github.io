from pathlib import Path
import sqlite3
import pandas as pd


# -----------------------------
# Paths
# -----------------------------

project_root = Path(__file__).resolve().parent.parent

data_dir = project_root / "data"

database_dir = project_root / "database"

database_dir.mkdir(exist_ok=True)


db_path = database_dir / "fraud_detection.db"


# -----------------------------
# Load Data
# -----------------------------

df = pd.read_csv(
    data_dir / "featured_train.csv"
)


# Keep important transaction fields

columns = [
    "TransactionID",
    "TransactionAmt",
    "ProductCD",
    "card4",
    "DeviceType",
    "P_emaildomain",
    "isFraud"
]


transactions = df[columns]


# -----------------------------
# Create SQLite Database
# -----------------------------

connection = sqlite3.connect(
    db_path
)


transactions.to_sql(
    "transactions",
    connection,
    if_exists="replace",
    index=False
)


connection.close()


print("Database created!")
print(db_path)