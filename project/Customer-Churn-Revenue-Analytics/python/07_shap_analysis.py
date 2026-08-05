import pandas as pd
import numpy as np

import shap

import joblib

import matplotlib.pyplot as plt

import os


# =========================
# LOAD DATA
# =========================

df = pd.read_csv(
    "data/cleaned/customer_churn_clean.csv"
)


# =========================
# LOAD MODEL
# =========================

model = joblib.load(
    "models/churn_model.pkl"
)


print("Model Loaded")



# =========================
# PREPARE FEATURES
# =========================


X = df.drop(
    columns=[
        "Customer_ID",
        "Customer_Churn",
        "Churn_Flag"
    ],
    errors="ignore"
)


# =========================
# CREATE PREDICTIONS
# =========================


probabilities = model.predict_proba(X)[:,1]


df["Churn_Probability"] = probabilities



# =========================
# CREATE RISK LEVEL
# =========================


def risk_level(prob):

    if prob >= 0.75:
        return "High Risk"

    elif prob >= 0.40:
        return "Medium Risk"

    else:
        return "Low Risk"



df["Risk_Level"] = (
    df["Churn_Probability"]
    .apply(risk_level)
)



# =========================
# REVENUE AT RISK
# =========================


df["Revenue_At_Risk"] = (

    df["Monthly_Revenue"]

    *

    df["Churn_Probability"]

)



print("\nRisk Distribution")

print(
    df["Risk_Level"]
    .value_counts()
)



print("\nRevenue Exposure:")

print(

    df["Revenue_At_Risk"]
    .sum()

)



# =========================
# SAVE CUSTOMER RISK FILE
# =========================


os.makedirs(
    "data/analytics",
    exist_ok=True
)


df.to_csv(

    "data/analytics/customer_risk_scores.csv",

    index=False

)



# =========================
# SHAP EXPLANATION
# =========================


print("\nCreating SHAP Explanation")



# Get transformed data

preprocessor = model.named_steps[
    "preprocessor"
]


classifier = model.named_steps[
    "model"
]



X_encoded = preprocessor.transform(X)



explainer = shap.TreeExplainer(
    classifier
)



shap_values = explainer(
    X_encoded
)



os.makedirs(
    "images",
    exist_ok=True
)



plt.figure()


shap.summary_plot(

    shap_values,

    X_encoded,

    show=False

)


plt.tight_layout()


plt.savefig(

    "images/shap_feature_importance.png",

    bbox_inches="tight"

)


plt.close()



print("\nSHAP Complete!")
