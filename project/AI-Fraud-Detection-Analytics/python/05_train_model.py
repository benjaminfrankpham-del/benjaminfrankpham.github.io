from pathlib import Path
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    classification_report,
    roc_auc_score,
    confusion_matrix
)

from xgboost import XGBClassifier
import joblib


# -----------------------------
# Paths
# -----------------------------

project_root = Path(__file__).resolve().parent.parent

data_dir = project_root / "data"
model_dir = project_root / "models"

model_dir.mkdir(exist_ok=True)


# -----------------------------
# Load Dataset
# -----------------------------

df = pd.read_csv(
    data_dir / "featured_train.csv"
)

print("Dataset Shape:", df.shape)


# -----------------------------
# Separate Features and Target
# -----------------------------

X = df.drop(
    columns=["isFraud", "TransactionID"]
)

y = df["isFraud"]


print("\nFraud Distribution:")
print(y.value_counts())


# -----------------------------
# Handle Categorical Columns
# -----------------------------

X = pd.get_dummies(
    X,
    drop_first=True
)


print("\nAfter Encoding:")
print(X.shape)


# -----------------------------
# Train Test Split
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


print("\nTraining Size:", X_train.shape)
print("Testing Size:", X_test.shape)


# -----------------------------
# Train XGBoost Model
# -----------------------------

model = XGBClassifier(

    n_estimators=300,

    max_depth=6,

    learning_rate=0.05,

    subsample=0.8,

    colsample_bytree=0.8,

    scale_pos_weight=(
        len(y_train[y_train == 0]) /
        len(y_train[y_train == 1])
    ),

    eval_metric="auc",

    random_state=42

)


print("\nTraining model...")

model.fit(
    X_train,
    y_train
)


# -----------------------------
# Predictions
# -----------------------------

predictions = model.predict(
    X_test
)

probabilities = model.predict_proba(
    X_test
)[:,1]


# -----------------------------
# Evaluation
# -----------------------------

print("\nClassification Report")
print(
    classification_report(
        y_test,
        predictions
    )
)


auc = roc_auc_score(
    y_test,
    probabilities
)

print(
    f"\nROC-AUC Score: {auc:.4f}"
)


print("\nConfusion Matrix")

print(
    confusion_matrix(
        y_test,
        predictions
    )
)


# -----------------------------
# Save Model
# -----------------------------

joblib.dump(
    model,
    model_dir / "fraud_detection_xgb.pkl"
)


print("\nModel saved!")
