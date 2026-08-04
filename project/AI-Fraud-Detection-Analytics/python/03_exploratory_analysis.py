from pathlib import Path
import pandas as pd

# -----------------------------
# Project Paths
# -----------------------------
project_root = Path(__file__).resolve().parent.parent
data_dir = project_root / "data"
analysis_dir = project_root / "analysis"

# Create analysis folder if it doesn't exist
analysis_dir.mkdir(exist_ok=True)

# -----------------------------
# Load Cleaned Dataset
# -----------------------------
df = pd.read_csv(data_dir / "cleaned_train.csv")

print("=" * 60)
print("DATASET OVERVIEW")
print("=" * 60)

print(f"Rows: {df.shape[0]:,}")
print(f"Columns: {df.shape[1]}")

print("\nData Types")
print(df.dtypes.value_counts())

print("\nMissing Values (Top 20)")
missing = df.isnull().sum().sort_values(ascending=False)
print(missing.head(20))

# -----------------------------
# Fraud Distribution
# -----------------------------
print("\n" + "=" * 60)
print("FRAUD DISTRIBUTION")
print("=" * 60)

fraud_counts = df["isFraud"].value_counts()
fraud_rate = df["isFraud"].mean() * 100

print(fraud_counts)
print(f"\nFraud Rate: {fraud_rate:.2f}%")

fraud_counts.to_csv(
    analysis_dir / "fraud_counts.csv",
    header=["Count"]
)

# -----------------------------
# Transaction Amount Analysis
# -----------------------------
print("\n" + "=" * 60)
print("TRANSACTION AMOUNT")
print("=" * 60)

transaction_stats = (
    df.groupby("isFraud")["TransactionAmt"]
      .describe()
)

print(transaction_stats)

transaction_stats.to_csv(
    analysis_dir / "transaction_statistics.csv"
)

# -----------------------------
# Product Fraud Rate
# -----------------------------
print("\n" + "=" * 60)
print("PRODUCT FRAUD RATE")
print("=" * 60)

fraud_by_product = (
    df.groupby("ProductCD")["isFraud"]
      .agg(
          Transactions="count",
          FraudRate="mean"
      )
      .sort_values("FraudRate", ascending=False)
)

print(fraud_by_product)

fraud_by_product.to_csv(
    analysis_dir / "fraud_by_product.csv"
)

# -----------------------------
# Card Brand Fraud Rate
# -----------------------------
print("\n" + "=" * 60)
print("CARD BRAND FRAUD RATE")
print("=" * 60)

fraud_by_card = (
    df.groupby("card4")["isFraud"]
      .agg(
          Transactions="count",
          FraudRate="mean"
      )
      .sort_values("FraudRate", ascending=False)
)

print(fraud_by_card)

fraud_by_card.to_csv(
    analysis_dir / "fraud_by_card.csv"
)

# -----------------------------
# Email Domain Risk
# -----------------------------
print("\n" + "=" * 60)
print("TOP EMAIL DOMAIN FRAUD RATES")
print("=" * 60)

email_risk = (
    df.groupby("P_emaildomain")["isFraud"]
      .agg(
          Transactions="count",
          FraudRate="mean"
      )
      .sort_values("FraudRate", ascending=False)
)

print(email_risk.head(20))

email_risk.to_csv(
    analysis_dir / "email_risk.csv"
)

# -----------------------------
# Device Risk
# -----------------------------
if "DeviceType" in df.columns:

    print("\n" + "=" * 60)
    print("DEVICE TYPE FRAUD RATE")
    print("=" * 60)

    device_risk = (
        df.groupby("DeviceType")["isFraud"]
          .agg(
              Transactions="count",
              FraudRate="mean"
          )
          .sort_values("FraudRate", ascending=False)
    )

    print(device_risk)

    device_risk.to_csv(
        analysis_dir / "device_risk.csv"
    )

print("\n" + "=" * 60)
print("EDA COMPLETE")
print("=" * 60)

print("\nFiles created:")

for file in analysis_dir.glob("*.csv"):
    print("✓", file.name)