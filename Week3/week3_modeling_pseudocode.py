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
