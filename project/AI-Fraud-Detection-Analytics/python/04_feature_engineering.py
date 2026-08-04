from pathlib import Path
import pandas as pd
import numpy as np

# -----------------------------
# Project Paths
# -----------------------------
project_root = Path(__file__).resolve().parent.parent
data_dir = project_root / "data"

# -----------------------------
# Load Clean Dataset
# -----------------------------
df = pd.read_csv(data_dir / "cleaned_train.csv")

print(f"Original Shape: {df.shape}")

# =====================================================
# AMOUNT FEATURES
# =====================================================

# Log transaction amount
df["TransactionAmt_Log"] = np.log1p(df["TransactionAmt"])

# High value transaction (top 5%)
high_amount = df["TransactionAmt"].quantile(0.95)

df["HighAmountFlag"] = (
    df["TransactionAmt"] >= high_amount
).astype(int)

# =====================================================
# DEVICE FEATURES
# =====================================================

df["IsMobile"] = (
    df["DeviceType"] == "mobile"
).astype(int)

df["IsDesktop"] = (
    df["DeviceType"] == "desktop"
).astype(int)

df["MissingDevice"] = (
    df["DeviceType"].isna()
).astype(int)

# =====================================================
# EMAIL FEATURES
# =====================================================

df["UsesGmail"] = (
    df["P_emaildomain"] == "gmail.com"
).astype(int)

df["UsesYahoo"] = (
    df["P_emaildomain"].str.contains("yahoo", na=False)
).astype(int)

df["UsesOutlook"] = (
    df["P_emaildomain"].str.contains("outlook", na=False)
).astype(int)

df["MissingEmail"] = (
    df["P_emaildomain"].isna()
).astype(int)

# =====================================================
# PRODUCT FEATURES
# =====================================================

df["HighRiskProduct"] = (
    df["ProductCD"] == "C"
).astype(int)

# =====================================================
# CARD FEATURES
# =====================================================

df["IsVisa"] = (
    df["card4"] == "visa"
).astype(int)

df["IsMastercard"] = (
    df["card4"] == "mastercard"
).astype(int)

df["IsDiscover"] = (
    df["card4"] == "discover"
).astype(int)

df["IsAmex"] = (
    df["card4"] == "american express"
).astype(int)

# =====================================================
# DISTANCE FEATURES
# =====================================================

df["HasDistance"] = (
    df["dist1"].notna()
).astype(int)

# =====================================================
# MISSING VALUE FLAGS
# =====================================================

df["MissingAddr1"] = (
    df["addr1"].isna()
).astype(int)

df["MissingAddr2"] = (
    df["addr2"].isna()
).astype(int)

# =====================================================
# SAVE FEATURED DATASET
# =====================================================

print(f"New Shape: {df.shape}")

print(f"Features Added: {df.shape[1]-434}")

df.to_csv(
    data_dir / "featured_train.csv",
    index=False
)

print("\nFeature Engineering Complete!")
print("featured_train.csv saved successfully.")