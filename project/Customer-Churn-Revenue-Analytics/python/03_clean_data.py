import pandas as pd


# =========================
# LOAD DATA
# =========================

df = pd.read_excel(
    "data/raw/telco_customer_churn.xlsx"
)


print("Original Shape:")
print(df.shape)


# =========================
# RENAME COLUMNS
# =========================

df = df.rename(columns={

    "CustomerID": "Customer_ID",

    "Gender": "Customer_Gender",

    "Senior Citizen": "Senior_Customer",

    "Partner": "Has_Partner",

    "Dependents": "Has_Dependents",

    "Tenure Months": "Customer_Tenure_Months",

    "Phone Service": "Phone_Service",

    "Multiple Lines": "Multiple_Lines",

    "Internet Service": "Digital_Service",

    "Online Security": "Security_Product",

    "Online Backup": "Backup_Product",

    "Device Protection": "Device_Protection",

    "Tech Support": "Customer_Support",

    "Streaming TV": "Entertainment_Service",

    "Streaming Movies": "Media_Service",

    "Contract": "Account_Contract",

    "Paperless Billing": "Digital_Billing",

    "Payment Method": "Payment_Method",

    "Monthly Charges": "Monthly_Revenue",

    "Total Charges": "Lifetime_Revenue",

    "Churn Label": "Customer_Churn",

    "Churn Value": "Churn_Flag",

    "CLTV": "Customer_Lifetime_Value"

})


# =========================
# REMOVE UNUSED COLUMNS
# =========================

remove_columns = [

    "Count",

    "Country",

    "Lat Long",

    "Latitude",

    "Longitude",

    "Churn Score",

    "Churn Reason"

]


df = df.drop(
    columns=remove_columns,
    errors="ignore"
)


# =========================
# FIX DATA TYPES
# =========================

df["Lifetime_Revenue"] = pd.to_numeric(
    df["Lifetime_Revenue"],
    errors="coerce"
)


# Fill missing lifetime revenue

df["Lifetime_Revenue"] = (
    df["Lifetime_Revenue"]
    .fillna(0)
)


# =========================
# CREATE BUSINESS FEATURES
# =========================


# Customer Tenure Category

df["Tenure_Category"] = pd.cut(
    df["Customer_Tenure_Months"],
    bins=[
        -1,
        12,
        36,
        60,
        72
    ],
    labels=[
        "New Customer",
        "Established Customer",
        "Loyal Customer",
        "Long-Term Customer"
    ]
)


# Revenue Segment

df["Revenue_Segment"] = pd.cut(
    df["Monthly_Revenue"],
    bins=[
        0,
        50,
        100,
        200
    ],
    labels=[
        "Low Revenue",
        "Medium Revenue",
        "High Revenue"
    ]
)


# Customer Value Segment

df["Customer_Value_Segment"] = pd.cut(
    df["Customer_Lifetime_Value"],
    bins=[
        0,
        3000,
        5000,
        7000
    ],
    labels=[
        "Standard Value",
        "High Value",
        "Premium Value"
    ]
)


# =========================
# SAVE CLEAN DATA
# =========================

df.to_csv(
    "data/cleaned/customer_churn_clean.csv",
    index=False
)


print("\nClean Dataset Shape:")
print(df.shape)


print("\nColumns:")
print(df.columns.tolist())


print("\nCleaning Complete!")