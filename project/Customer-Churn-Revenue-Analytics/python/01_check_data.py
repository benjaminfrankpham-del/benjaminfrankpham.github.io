import pandas as pd

# Load the dataset
df = pd.read_excel("data/raw/telco_customer_churn.xlsx")

# Display basic information
print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())