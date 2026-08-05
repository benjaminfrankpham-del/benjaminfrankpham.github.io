import pandas as pd
import matplotlib.pyplot as plt
import os


# =========================
# LOAD DATA
# =========================

df = pd.read_csv(
    "data/cleaned/customer_churn_clean.csv"
)


# Create images folder

os.makedirs(
    "images",
    exist_ok=True
)


# =========================
# 1. CHURN DISTRIBUTION
# =========================

churn_counts = (
    df["Customer_Churn"]
    .value_counts()
)


plt.figure(figsize=(7,5))

plt.bar(
    churn_counts.index,
    churn_counts.values
)

plt.title(
    "Customer Churn Distribution"
)

plt.xlabel(
    "Customer Status"
)

plt.ylabel(
    "Number of Customers"
)

plt.tight_layout()

plt.savefig(
    "images/churn_distribution.png"
)

plt.close()



# =========================
# 2. CONTRACT CHURN ANALYSIS
# =========================

contract_churn = (
    df.groupby(
        "Account_Contract"
    )["Churn_Flag"]
    .mean()
    * 100
)


plt.figure(figsize=(8,5))

plt.bar(
    contract_churn.index,
    contract_churn.values
)

plt.title(
    "Churn Rate by Contract Type"
)

plt.xlabel(
    "Contract Type"
)

plt.ylabel(
    "Churn Rate (%)"
)

plt.xticks(
    rotation=45
)

plt.tight_layout()

plt.savefig(
    "images/contract_churn.png"
)

plt.close()



# =========================
# 3. REVENUE SEGMENT ANALYSIS
# =========================

revenue_segment = (
    df.groupby(
        "Customer_Value_Segment"
    )["Monthly_Revenue"]
    .sum()
)


plt.figure(figsize=(8,5))

plt.bar(
    revenue_segment.index.astype(str),
    revenue_segment.values
)

plt.title(
    "Monthly Revenue by Customer Segment"
)

plt.xlabel(
    "Customer Segment"
)

plt.ylabel(
    "Monthly Revenue"
)

plt.xticks(
    rotation=45
)

plt.tight_layout()

plt.savefig(
    "images/revenue_segments.png"
)

plt.close()



# =========================
# 4. TENURE ANALYSIS
# =========================

tenure_churn = (
    df.groupby(
        "Tenure_Category"
    )["Churn_Flag"]
    .mean()
    * 100
)


plt.figure(figsize=(8,5))

plt.bar(
    tenure_churn.index.astype(str),
    tenure_churn.values
)

plt.title(
    "Churn Rate by Customer Tenure"
)

plt.xlabel(
    "Tenure Segment"
)

plt.ylabel(
    "Churn Rate (%)"
)

plt.xticks(
    rotation=45
)

plt.tight_layout()

plt.savefig(
    "images/tenure_analysis.png"
)

plt.close()



# =========================
# 5. PAYMENT METHOD ANALYSIS
# =========================

payment_churn = (
    df.groupby(
        "Payment_Method"
    )["Churn_Flag"]
    .mean()
    * 100
)


plt.figure(figsize=(9,5))

plt.bar(
    payment_churn.index.astype(str),
    payment_churn.values
)

plt.title(
    "Churn Rate by Payment Method"
)

plt.xlabel(
    "Payment Method"
)

plt.ylabel(
    "Churn Rate (%)"
)

plt.xticks(
    rotation=45
)

plt.tight_layout()

plt.savefig(
    "images/payment_churn.png"
)

plt.close()


print("EDA Analysis Complete!")
print("Charts saved in images/")