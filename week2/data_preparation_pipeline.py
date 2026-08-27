

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import KNNImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# ==========================================
# 1. DATA INGESTION
# ==========================================
def load_data(filepath: str) -> pd.DataFrame:
    """Loads the raw agricultural CSV data."""
    print(f"Loading data from {filepath}...")
    df = pd.read_csv(filepath)
    print(f"Raw data shape: {df.shape}")
    return df

# ==========================================
# 2. DOMAIN-SPECIFIC CLEANING
# ==========================================
def clean_agronomic_anomalies(df: pd.DataFrame) -> pd.DataFrame:
    """Applies agronomic hard bounds to correct sensor/data entry errors."""
    df = df.copy()
    
    # Cap Soil pH to realistic agricultural bounds (3.5 to 9.5)
    df['Soil_pH'] = df['Soil_pH'].clip(lower=3.5, upper=9.5)
    
    # Cap extreme rainfall anomalies (e.g., > 500mm/day is likely a sensor error)
    df['Rainfall_mm'] = df['Rainfall_mm'].clip(upper=500.0)
    
    # Remove negative yields (data entry errors)
    df = df[df['Yield_t_ha'] >= 0]
    
    # Standardize text formatting for crop names
    if 'Crop_Type' in df.columns:
        df['Crop_Type'] = df['Crop_Type'].str.strip().str.lower()
        
    return df

# ==========================================
# 3. FEATURE ENGINEERING
# ==========================================
def engineer_agri_features(df: pd.DataFrame) -> pd.DataFrame:
    """Creates new features based on agronomic domain knowledge."""
    df = df.copy()
    
    # Nutrient balance ratios
    df['N_P_Ratio'] = df['Nitrogen_N'] / (df['Phosphorus_P'] + 1e-5) # Avoid division by zero
    
    # Thermal stress proxy (High temp + low humidity)
    if 'Temperature_C' in df.columns and 'Humidity_pct' in df.columns:
        df['Thermal_Stress_Index'] = df['Temperature_C'] * (100 - df['Humidity_pct']) / 100
        
    return df

# ==========================================
# 4. PREPROCESSING PIPELINE
# ==========================================
def build_preprocessing_pipeline() -> ColumnTransformer:
    """Builds a scikit-learn pipeline for imputation, scaling, and encoding."""
    
    # Define column types
    numeric_features = ['Nitrogen_N', 'Phosphorus_P', 'Potassium_K', 
                        'Soil_pH', 'Rainfall_mm', 'Temperature_C', 'Humidity_pct']
    categorical_features = ['Season', 'Soil_Type']
    
    # Numeric pipeline: KNN Imputation + Standard Scaling
    numeric_transformer = Pipeline(steps=[
        ('imputer', KNNImputer(n_neighbors=5, weights='distance')),
        ('scaler', StandardScaler())
    ])
    
    # Categorical pipeline: Median Imputation (mode) + One-Hot Encoding
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
    ])
    
    # Combine into a preprocessor
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ])
        
    return preprocessor

# ==========================================
# 5. MAIN EXECUTION
# ==========================================
def main():
    # Simulate file path
    raw_data_path = 'data/raw_agri_data.csv'
    
    try:
        # Step 1: Load
        df = load_data(raw_data_path)
        
        # Step 2: Clean Anomalies
        df_clean = clean_agronomic_anomalies(df)
        
        # Step 3: Drop rows where the TARGET variable is missing
        df_clean = df_clean.dropna(subset=['Yield_t_ha', 'Crop_Type'])
        
        # Step 4: Feature Engineering
        df_final = engineer_agri_features(df_clean)
        
        # Step 5: Split Features (X) and Targets (y)
        # Note: In a real scenario, we would separate Classification (Crop) and Regression (Yield)
        X = df_final.drop(columns=['Yield_t_ha', 'Crop_Type'])
        y_class = df_final['Crop_Type']
        
        # Step 6: Train/Test Split (Stratified for classification)
        X_train, X_test, y_train, y_test = train_test_split(
            X, y_class, test_size=0.2, random_state=42, stratify=y_class
        )
        
        # Step 7: Apply Preprocessing Pipeline
        preprocessor = build_preprocessing_pipeline()
        X_train_processed = preprocessor.fit_transform(X_train)
        X_test_processed = preprocessor.transform(X_test)
        
        print("Data preparation pipeline executed successfully!")
        print(f"Processed Training Set Shape: {X_train_processed.shape}")
        print(f"Processed Testing Set Shape: {X_test_processed.shape}")
        
    except FileNotFoundError:
        print(f"Note: '{raw_data_path}' not found. This script serves as the structural template for the pipeline.")
        print("Please place the raw CSV in the 'data/' directory to run the full execution.")

if __name__ == "__main__":
    main()
