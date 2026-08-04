from pathlib import Path
import pandas as pd
import joblib
import shap


# -----------------------------
# Paths
# -----------------------------

project_root = Path(__file__).resolve().parent.parent

data_dir = project_root / "data"
model_dir = project_root / "models"


# -----------------------------
# Load Model
# -----------------------------

model = joblib.load(
    model_dir / "fraud_detection_xgb.pkl"
)

print("Model loaded successfully")


# -----------------------------
# Load Featured Data
# -----------------------------

df = pd.read_csv(
    data_dir / "featured_train.csv"
)

print("Dataset Loaded")
print(df.shape)


# -----------------------------
# Prepare Features
# -----------------------------

X = df.drop(
    columns=[
        "isFraud",
        "TransactionID"
    ]
)


# Apply same encoding as training

X = pd.get_dummies(
    X,
    drop_first=True
)


print("Encoded Shape:")
print(X.shape)


# -----------------------------
# Align Features With Model
# -----------------------------

model_features = model.get_booster().feature_names

X = X.reindex(
    columns=model_features,
    fill_value=0
)


# -----------------------------
# Pick Sample Transaction
# -----------------------------

sample = X.iloc[[0]]

transaction_id = df.iloc[0]["TransactionID"]


# -----------------------------
# Prediction
# -----------------------------

fraud_probability = model.predict_proba(
    sample
)[0][1]


print("\nTransaction ID:")
print(transaction_id)

print(
    f"\nFraud Probability: {fraud_probability:.2%}"
)


# -----------------------------
# SHAP Explanation
# -----------------------------

explainer = shap.TreeExplainer(
    model
)

shap_values = explainer(
    sample
)


# Get feature importance

importance = pd.DataFrame({

    "Feature":
        sample.columns,

    "SHAP_Value":
        shap_values.values[0]

})


importance["Impact"] = (
    importance["SHAP_Value"]
    .abs()
)


importance = importance.sort_values(
    "Impact",
    ascending=False
)


print("\nTop Fraud Factors:")

print(
    importance.head(10)
)


# Save explanation

importance.head(10).to_csv(
    project_root /
    "analysis" /
    "sample_fraud_explanation.csv",
    index=False
)


print(
    "\nExplanation saved!"
)