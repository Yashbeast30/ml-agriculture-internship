# Data Cleaning and Preparation Pipeline

This document outlines the step-by-step methodology used to transform the raw, messy agricultural data into a structured, model-ready format.

## Step 1: Standardization and Formatting
* **Action:** Convert all text-based categorical variables (e.g., Crop Names, Region Names) to lowercase and strip trailing whitespaces.
* **Action:** Standardize all temperature readings to Celsius and all precipitation metrics to millimeters (mm) to ensure uniform scale across merged datasets.

## Step 2: Handling Missing Values
Agricultural data requires context-aware imputation. Simple mean/median imputation can destroy seasonal patterns.
* **Weather Data (`Rainfall_mm`, `Temperature`):** Used **KNN (K-Nearest Neighbors) Imputation**. Since weather is spatially and temporally correlated, KNN finds plots with similar geographic and seasonal profiles to estimate the missing weather values accurately.
* **Soil Data (`Soil_pH`):** Used **Median Imputation**. Soil pH is a relatively static property per region, and median imputation prevents extreme outliers from skewing the fill value.
* **Target Variable (`Yield_t_ha`):** Records with missing target variables were **dropped**, as imputing the target variable would introduce severe data leakage and bias into the supervised learning models.

## Step 3: Outlier Treatment (Domain-Driven)
Instead of blindly dropping statistical outliers, agronomic hard bounds were applied (Winsorization/Capping):
* **Soil pH:** Capped at a minimum of 3.5 and a maximum of 9.5. Values outside this were flagged as sensor errors and set to the regional median.
* **Rainfall:** Daily rainfall exceeding the 99th percentile of historical regional maximums was capped at the 99th percentile value to prevent model distortion from sensor glitches.
* **Negative Yields:** Converted to absolute values where context suggested a sign error; otherwise, dropped.

## Step 4: Feature Engineering
To improve model performance, new agronomic features were engineered from the raw data:
1. **NPK Ratio:** Created `N_P_ratio` and `N_K_ratio` to capture nutrient balance, which is often more predictive of crop health than absolute raw numbers.
2. **Thermal Stress Index:** Engineered a feature combining high temperature and low humidity to simulate crop heat stress conditions.
3. **Water Availability Index:** Calculated as `(Rainfall_mm * Soil_Moisture) / Evapotranspiration_Rate`.

## Step 5: Encoding and Scaling
* **Categorical Encoding:** Applied **Target Encoding** for high-cardinality regional features, and **One-Hot Encoding** for the season/crop cycle categories.
* **Numerical Scaling:** Applied **StandardScaler** (Z-score normalization) to soil nutrients and weather features. Tree-based models (like Random Forest) do not strictly require scaling, but scaling ensures fair feature importance evaluation and is required for distance-based models like SVM or KNN.

## Step 6: Train/Test Split
* The data was split 80/20 into training and testing sets.
* **Stratified Sampling** was used based on the `Crop_Type` target to ensure that minority crops (e.g., specific pulses or niche cash crops) were proportionally represented in both sets.
