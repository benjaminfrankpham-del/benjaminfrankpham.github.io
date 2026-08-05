import pandas as pd


# Load dataset
df = pd.read_excel(
    "data/raw/telco_customer_churn.xlsx"
)


print("=" * 50)
print("DATASET OVERVIEW")
print("=" * 50)

print("\nShape:")
print(df.shape)


print("\nColumns:")
for col in df.columns:
    print(col)


print("\nData Types:")
print(df.dtypes)


print("\nMissing Values:")
print(df.isnull().sum())


print("\nDuplicate Rows:")
print(df.duplicated().sum())


print("\nDataset Summary:")
print(df.describe(include="all").transpose())


print("\nChurn Distribution:")
print(df["Churn Label"].value_counts())


print("\nChurn Percentage:")
print(
    df["Churn Label"]
    .value_counts(normalize=True)
    * 100
)