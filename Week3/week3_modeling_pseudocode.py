"""
Week 3: Simulated Data Analysis and Modeling Pipeline
Focus: Agriculture & Agribusiness

Tasks:
1. Crop suitability classification
2. Crop yield prediction
"""

# ============================================================
# 1. IMPORT LIBRARIES
# ============================================================

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    classification_report,
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# ============================================================
# 2. LOAD CLEANED DATA FROM WEEK 2
# ============================================================

# In a real project, this would load the cleaned dataset.
# df = pd.read_csv("data/clean_agriculture_data.csv")

# For simulation, we describe the expected structure.
print("Loading cleaned agricultural dataset...")

# Expected columns:
# Nitrogen, Phosphorus, Potassium, Soil_pH, Rainfall_mm,
# Temperature_C, Humidity_pct, Region, Season, Crop_Type, Yield_t_ha

# ============================================================
# 3. DEFINE FEATURES AND TARGETS
# ============================================================

# Example feature list
# numerical_features = [
#     "Nitrogen_N",
#     "Phosphorus_P",
#     "Potassium_K",
#     "Soil_pH",
#     "Rainfall_mm",
#     "Temperature_C",
#     "Humidity_pct"
# ]

# categorical_features = [
#     "Region",
#     "Season"
# ]

# Classification target:
# y_class = df["Crop_Type"]

# Regression target:
# y_reg = df["Yield_t_ha"]

# ============================================================
# 4. TRAIN TEST SPLIT
# ============================================================

# Classification split
# X_train_class, X_test_class, y_train_class, y_test_class = train_test_split(
#     X,
#     y_class,
#     test_size=0.2,
#     random_state=42,
#     stratify=y_class
# )

# Regression split
# X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(
#     X,
#     y_reg,
#     test_size=0.2,
#     random_state=42
# )

# ============================================================
# 5. PREPROCESSING PIPELINE
# ============================================================

# numeric_pipeline = Pipeline([
#     ("imputer", SimpleImputer(strategy="median")),
#     ("scaler", StandardScaler())
# ])

# categorical_pipeline = Pipeline([
#     ("imputer", SimpleImputer(strategy="most_frequent")),
#     ("onehot", OneHotEncoder(handle_unknown="ignore"))
# ])

# preprocessor = ColumnTransformer([
#     ("num", numeric_pipeline, numerical_features),
#     ("cat", categorical_pipeline, categorical_features)
# ])

# ============================================================
# 6. CLASSIFICATION MODEL
# ============================================================

# classification_pipeline = Pipeline([
#     ("preprocessor", preprocessor),
#     ("classifier", RandomForestClassifier(n_estimators=200, random_state=42))
# ])

# classification_pipeline.fit(X_train_class, y_train_class)
# y_pred_class = classification_pipeline.predict(X_test_class)

# accuracy = accuracy_score(y_test_class, y_pred_class)
# macro_f1 = f1_score(y_test_class, y_pred_class, average="macro")

# print("Classification Accuracy:", accuracy)
# print("Macro F1 Score:", macro_f1)
# print(classification_report(y_test_class, y_pred_class))

# ============================================================
# 7. REGRESSION MODEL
# ============================================================

# regression_pipeline = Pipeline([
#     ("preprocessor", preprocessor),
#     ("regressor", RandomForestRegressor(n_estimators=200, random_state=42))
# ])

# regression_pipeline.fit(X_train_reg, y_train_reg)
# y_pred_reg = regression_pipeline.predict(X_test_reg)

# mae = mean_absolute_error(y_test_reg, y_pred_reg)
# rmse = np.sqrt(mean_squared_error(y_test_reg, y_pred_reg))
# r2 = r2_score(y_test_reg, y_pred_reg)

# print("Regression MAE:", mae)
# print("Regression RMSE:", rmse)
# print("Regression R2:", r2)

# ============================================================
# 8. FEATURE IMPORTANCE
# ============================================================

# For Random Forest, feature importance can be extracted after fitting.

# feature_importances = classification_pipeline.named_steps["classifier"].feature_importances_

# importance_df = pd.DataFrame({
#     "feature": feature_names_after_preprocessing,
#     "importance": feature_importances
# }).sort_values("importance", ascending=False)

# print(importance_df.head())

# ============================================================
# 9. SIMULATED RESULTS SUMMARY
# ============================================================

simulated_results = {
    "classification": {
        "model": "Random Forest Classifier",
        "accuracy": 0.87,
        "macro_f1": 0.84
    },
    "regression": {
        "model": "Random Forest Regressor",
        "mae_tons_per_ha": 0.42,
        "rmse_tons_per_ha": 0.58,
        "r2": 0.81,
        "mape_percent": 12.4
    },
    "top_features": [
        "Rainfall_mm",
        "Nitrogen_N",
        "Temperature_C",
        "Soil_pH",
        "Humidity_pct"
    ]
}

print("Simulated Week 3 Modeling Results:")
print(simulated_results)
