import pandas as pd
import sqlite3
import os


# =========================
# FILE PATHS
# =========================

csv_file = "data/cleaned/customer_churn_clean.csv"

database_file = "database/customer_analytics.db"


# =========================
# LOAD CLEAN DATA
# =========================

df = pd.read_csv(csv_file)

print("Loaded Dataset:")
print(df.shape)


# =========================
# CREATE DATABASE
# =========================

# Remove old database if it exists

if os.path.exists(database_file):
    os.remove(database_file)


connection = sqlite3.connect(database_file)


# =========================
# CREATE TABLES
# =========================


customers = df[
    [
        "Customer_ID",
        "Customer_Gender",
        "Senior_Customer",
        "Has_Partner",
        "Has_Dependents",
        "City",
        "State",
        "Zip Code"
    ]
]


customers.to_sql(
    "customers",
    connection,
    index=False
)


accounts = df[
    [
        "Customer_ID",
        "Account_Contract",
        "Payment_Method",
        "Digital_Billing",
        "Customer_Tenure_Months"
    ]
]


accounts.to_sql(
    "accounts",
    connection,
    index=False
)


revenue = df[
    [
        "Customer_ID",
        "Monthly_Revenue",
        "Lifetime_Revenue",
        "Customer_Lifetime_Value",
        "Revenue_Segment",
        "Customer_Value_Segment"
    ]
]


revenue.to_sql(
    "revenue",
    connection,
    index=False
)


behavior = df[
    [
        "Customer_ID",
        "Phone_Service",
        "Digital_Service",
        "Security_Product",
        "Backup_Product",
        "Device_Protection",
        "Customer_Support",
        "Entertainment_Service",
        "Media_Service"
    ]
]


behavior.to_sql(
    "customer_behavior",
    connection,
    index=False
)


churn = df[
    [
        "Customer_ID",
        "Customer_Churn",
        "Churn_Flag",
        "Tenure_Category"
    ]
]


churn.to_sql(
    "churn_analysis",
    connection,
    index=False
)



# =========================
# VERIFY DATABASE
# =========================


cursor = connection.cursor()


cursor.execute(
    """
    SELECT name 
    FROM sqlite_master
    WHERE type='table';
    """
)


tables = cursor.fetchall()


print("\nDatabase Tables:")

for table in tables:
    print(table[0])


connection.close()


print("\nDatabase creation complete!")