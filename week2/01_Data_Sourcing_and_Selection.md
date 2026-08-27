# Week 2: Data Sourcing and Selection Strategy

## 1. Introduction
The foundation of any robust machine learning pipeline in agribusiness is high-quality, relevant data. This document outlines the strategy, criteria, and sources used to acquire the agricultural datasets for this project. The focus is on simulating a realistic data acquisition pipeline that addresses core agribusiness challenges: **crop suitability classification** and **yield optimization**.

## 2. Data Selection Criteria
To ensure the data is practical for machine learning and relevant to the agricultural domain, the following criteria were applied during the sourcing phase:

1. **Domain Relevance:** The dataset must contain agronomic features (e.g., soil NPK levels, pH, weather variables) that directly influence crop growth and yield.
2. **Accessibility & Licensing:** Data must be publicly available, open-source, and permissible for commercial/educational use (e.g., CC0, MIT, or public domain).
3. **Granularity:** The data should ideally be at the farm, regional, or plot level rather than purely macroeconomic (country-level) to allow for actionable, localized ML predictions.
4. **Completeness:** While missing values are expected and will be cleaned, the core features (target variable and primary predictors) must have at least 70% complete records.

## 3. Selected Data Sources

### 3.1 Primary Dataset: Crop Recommendation & Soil Health Dataset
* **Source:** Kaggle / Agricultural Research Institutes (Simulated open-source equivalent)
* **Description:** Contains plot-level soil nutrient data (Nitrogen, Phosphorus, Potassium), soil pH, and localized weather metrics (temperature, humidity, rainfall) mapped to optimal crop types.
* **Relevance:** Directly addresses the classification objective (Crop Suitability) and input optimization (fertilizer usage).
* **Format:** CSV, ~2,200 records, 8 features.

### 3.2 Secondary Dataset: Historical Crop Yield Statistics
* **Source:** FAOSTAT (Food and Agriculture Organization of the UN)
* **Description:** Annual crop production and yield (tonnes/hectare) data aggregated by region and year.
* **Relevance:** Provides the continuous target variable required for the regression objective (Yield Prediction).
* **Format:** CSV / API, highly aggregated.

### 3.3 Supplementary Dataset: Meteorological & Climate Data
* **Source:** NASA POWER (Prediction Of Worldwide Energy Resources)
* **Description:** Daily and monthly historical weather data, including solar radiation, evapotranspiration, and precipitation.
* **Relevance:** Used to enrich the primary dataset with advanced weather features that impact crop stress and growth cycles.
* **Format:** API / NetCDF / CSV.

## 4. Data Integration Strategy
Because agricultural data is notoriously siloed, the primary challenge in Week 2 is merging these sources. The integration strategy relies on **spatial and temporal keys**:
* **Spatial:** Mapping regional codes (e.g., State/District IDs) from FAOSTAT to the plot-level data.
* **Temporal:** Aggregating daily NASA POWER weather data into "growing season" averages to match the annual harvest cycles in the FAOSTAT yield data.
