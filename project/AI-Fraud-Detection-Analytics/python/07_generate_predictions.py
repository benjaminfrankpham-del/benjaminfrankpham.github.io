from pathlib import Path
import pandas as pd
import joblib
import sqlite3


# -----------------------------
# Paths
# -----------------------------

project_root = Path(__file__).resolve().parent.parent

data_dir = project_root / "data"
model_dir = project_root / "models"
database_dir = project_root / "database"


# -----------------------------
# Load Model
# -----------------------------

model = joblib.load(
    model_dir / "fraud_detection_xgb.pkl"
)

print("Model loaded")


# -----------------------------
# Load Dataset
# -----------------------------

df = pd.read_csv(
    data_dir / "featured_train.csv"
)

print("Dataset loaded")
print(df.shape)


# -----------------------------
# Prepare Features
# -----------------------------

transaction_ids = df["TransactionID"]

actual_fraud = df["isFraud"]


X = df.drop(
    columns=[
        "isFraud",
        "TransactionID"
    ]
)


# Same encoding as training

X = pd.get_dummies(
    X,
    drop_first=True
)


# Match model features

model_features = (
    model.get_booster()
    .feature_names
)


X = X.reindex(
    columns=model_features,
    fill_value=0
)


# -----------------------------
# Generate Predictions
# -----------------------------

fraud_probability = (
    model.predict_proba(X)[:,1]
)


predicted_class = (
    fraud_probability >= 0.5
).astype(int)


# -----------------------------
# Create Risk Categories
# -----------------------------

def assign_risk(score):

    if score >= 0.80:
        return "High"

    elif score >= 0.40:
        return "Medium"

    else:
        return "Low"



risk_level = (
    pd.Series(fraud_probability)
    .apply(assign_risk)
)


# -----------------------------
# Create Prediction Table
# -----------------------------

predictions = pd.DataFrame({

    "TransactionID": transaction_ids,

    "Fraud_Probability":
        fraud_probability,

    "Risk_Level":
        risk_level,

    "Model_Prediction":
        predicted_class,

    "Actual_Fraud":
        actual_fraud

})


print(predictions.head())


# -----------------------------
# Save CSV
# -----------------------------

predictions.to_csv(
    data_dir / "model_predictions.csv",
    index=False
)


# -----------------------------
# Load Into SQLite
# -----------------------------

db_path = (
    database_dir /
    "fraud_detection.db"
)


connection = sqlite3.connect(
    db_path
)


predictions.to_sql(
    "model_predictions",
    connection,
    if_exists="replace",
    index=False
)


connection.close()


print("\nPredictions table created!")