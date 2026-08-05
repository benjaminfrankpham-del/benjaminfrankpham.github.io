import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import OneHotEncoder

from sklearn.compose import ColumnTransformer

from sklearn.pipeline import Pipeline

from sklearn.metrics import (
    classification_report,
    roc_auc_score,
    confusion_matrix
)

from sklearn.linear_model import LogisticRegression

from sklearn.ensemble import RandomForestClassifier

from xgboost import XGBClassifier

import joblib


# =========================
# LOAD DATA
# =========================

df = pd.read_csv(
    "data/cleaned/customer_churn_clean.csv"
)


print("Dataset Shape:")
print(df.shape)



# =========================
# REMOVE DATA LEAKAGE
# =========================

remove_columns = [

    "Customer_ID",

    "Customer_Churn",

    "Churn_Flag",

]


df = df.drop(
    columns=remove_columns,
    errors="ignore"
)



# =========================
# TARGET
# =========================

y = pd.read_csv(
    "data/cleaned/customer_churn_clean.csv"
)["Churn_Flag"]


X = df



# =========================
# IDENTIFY FEATURES
# =========================


categorical_features = X.select_dtypes(
    include="object"
).columns


numeric_features = X.select_dtypes(
    include=[
        "int64",
        "float64"
    ]
).columns



# =========================
# PREPROCESSING
# =========================


preprocessor = ColumnTransformer(

    transformers=[

        (
            "cat",
            OneHotEncoder(
                handle_unknown="ignore"
            ),
            categorical_features
        ),

        (
            "num",
            "passthrough",
            numeric_features
        )

    ]

)



# =========================
# SPLIT DATA
# =========================


X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.2,

    random_state=42,

    stratify=y

)



# =========================
# MODELS
# =========================


models = {


"Logistic Regression":

LogisticRegression(
    max_iter=1000
),



"Random Forest":

RandomForestClassifier(
    n_estimators=300,
    random_state=42
),



"XGBoost":

XGBClassifier(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=4,
    random_state=42
)


}



results = {}

trained_models = {}


# =========================
# TRAIN MODELS
# =========================


for name, model in models.items():


    print("\n====================")

    print(name)

    print("====================")


    pipeline = Pipeline(

        steps=[

            (
                "preprocessor",
                preprocessor
            ),

            (
                "model",
                model
            )

        ]

    )


    pipeline.fit(
        X_train,
        y_train
    )

    trained_models[name] = pipeline


    predictions = pipeline.predict(
        X_test
    )


    probabilities = pipeline.predict_proba(
        X_test
    )[:,1]



    auc = roc_auc_score(
        y_test,
        probabilities
    )


    results[name] = auc


    print(
        classification_report(
            y_test,
            predictions
        )
    )


    print(
        "ROC-AUC:",
        auc
    )



# =========================
# SAVE BEST MODEL
# =========================


best_model = max(
    results,
    key=results.get
)


print("\nBest Model:")
print(best_model)


joblib.dump(
    trained_models[best_model],
    "models/churn_model.pkl"
)


print(
    "Model saved!"
)