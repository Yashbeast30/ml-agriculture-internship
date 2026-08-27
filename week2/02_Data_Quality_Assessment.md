# Data Quality Assessment and Profiling

## 1. Initial Data Profiling
Before applying any cleaning techniques, a comprehensive data profiling exercise was conducted to understand the raw state of the acquired datasets. Below is the simulated assessment of the primary merged dataset (`raw_agri_data.csv`).

### 1.1 Dataset Dimensions
* **Total Records:** 2,200 (Plot-level observations)
* **Total Features:** 12 (Soil metrics, weather metrics, target crop, target yield)

### 1.2 Missingness Analysis
| Feature | Missing % | Agronomic Context & Impact |
|---|---|---|
| `Rainfall_mm` | 4.5% | Missing due to sensor downtime. Critical for yield prediction; requires careful imputation. |
| `Soil_pH` | 1.2% | Missing due to lab testing errors. Important for crop suitability classification. |
| `Potassium_K` | 0.0% | Fully populated. |
| `Yield_t_ha` | 15.0% | High missingness in secondary FAOSTAT data due to unreported regional harvests. |

### 1.3 Outlier and Anomaly Detection
Using domain knowledge and statistical profiling, the following anomalies were identified:
1. **Impossible Soil pH Values:** 8 records showed a pH < 0 or > 14. (Agronomic reality: agricultural soil pH ranges from 3.5 to 9.5).
2. **Extreme Rainfall Spikes:** 12 records showed daily rainfall > 500mm, which are likely sensor calibration errors rather than true meteorological events.
3. **Negative Yield Values:** 3 records in the FAOSTAT merge showed negative yield, resulting from data entry errors (e.g., subtracting crop losses incorrectly).

### 1.4 Inconsistencies and Formatting Issues
* **Unit Mismatches:** Temperature was recorded in Celsius in the primary dataset but Fahrenheit in the supplementary NASA data.
* **Categorical Inconsistencies:** Crop names had mixed casing and trailing spaces (e.g., `"maize"`, `"Maize "`, `"MAIZE"`).
