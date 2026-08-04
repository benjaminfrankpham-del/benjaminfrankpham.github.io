from pathlib import Path
import pandas as pd

# Project paths
project_root = Path(__file__).resolve().parent.parent
data_dir = project_root / "data"

# Load merged data
df = pd.read_csv(data_dir / "merged_train.csv")

print("Dataset Shape:", df.shape)

# Check missing values
missing = df.isnull().sum().sort_values(ascending=False)
print("\nTop 20 columns with missing values:")
print(missing.head(20))

# Remove duplicate transactions if any
df = df.drop_duplicates(subset="TransactionID")

print("\nDataset Shape After Removing Duplicates:", df.shape)

# Save cleaned dataset
df.to_csv(data_dir / "cleaned_train.csv", index=False)

print("\n Cleaned dataset saved as cleaned_train.csv")