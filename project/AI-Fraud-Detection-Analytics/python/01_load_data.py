import pandas as pd

# Load datasets
transactions = pd.read_csv("data/train_transaction.csv")
identity = pd.read_csv("data/train_identity.csv")

print("Transactions:", transactions.shape)
print("Identity:", identity.shape)

# Merge on TransactionID
df = transactions.merge(
    identity,
    on="TransactionID",
    how="left"
)

print("Merged:", df.shape)

# Save merged dataset
df.to_csv("data/merged_train.csv", index=False)

print("Merged dataset saved!")