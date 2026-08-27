# Week 3: Preliminary Data Exploration Plan

## 1. Purpose

The purpose of this exploration phase is to understand the patterns, distributions, relationships, and quality of the agricultural dataset prepared during Week 2. Since the dataset has already been cleaned and structured, this stage focuses on discovering insights that support machine learning model selection and business interpretation.

The exploration is based on the prepared agricultural dataset containing soil, weather, and crop-related features.

---

## 2. Dataset Used

The dataset used for Week 3 is the cleaned and structured dataset produced in Week 2.

### Main feature groups

| Feature Group | Example Variables |
|---|---|
| Soil features | Nitrogen, Phosphorus, Potassium, Soil pH |
| Weather features | Rainfall, Temperature, Humidity |
| Crop features | Crop type, Yield |
| Location features | Region, Agro-ecological zone |
| Time features | Season, Year |

---

## 3. Exploration Objectives

The data exploration process aims to answer the following questions:

1. Which soil features are most strongly related to crop yield?
2. Does rainfall have a strong positive relationship with yield?
3. Are there optimal ranges for soil pH and temperature?
4. Which crops are most common in the dataset?
5. Are there class imbalance issues in crop type?
6. Are there regional differences in productivity?
7. Are weather and soil features highly correlated?
8. Are there outliers that still affect modelling?
9. Which features may be most useful for classification and regression?
10. Can the data support practical agribusiness recommendations?

---

## 4. Exploratory Analysis Steps

### Step 1: Dataset overview

The dataset will be reviewed to confirm that it is ready for analysis.

Checks include:

- Number of rows and columns
- Feature names
- Data types
- Missing values
- Duplicate records
- Target variable availability

---

### Step 2: Univariate analysis

Univariate analysis examines each variable individually.

Planned visualisations:

| Feature | Chart Type | Purpose |
|---|---|---|
| Rainfall | Histogram | Understand rainfall distribution |
| Temperature | Histogram | Detect extreme temperature values |
| Soil pH | Box plot | Check realistic soil pH range |
| Nitrogen | Histogram | Understand nutrient distribution |
| Phosphorus | Histogram | Check nutrient spread |
| Potassium | Histogram | Detect unusual nutrient levels |
| Crop type | Count plot | Check crop class balance |
| Yield | Histogram | Understand productivity distribution |

---

### Step 3: Bivariate analysis

Bivariate analysis examines relationships between two variables.

Planned analysis:

| Relationship | Chart Type | Purpose |
|---|---|---|
| Rainfall vs Yield | Scatter plot | Check water availability effect |
| Nitrogen vs Yield | Scatter plot | Check nutrient impact |
| Temperature vs Yield | Scatter plot | Identify heat stress effect |
| Soil pH vs Crop type | Box plot | Identify crop pH preferences |
| Humidity vs Yield | Scatter plot | Check moisture-related effect |
| Region vs Yield | Bar plot | Compare regional productivity |

---

### Step 4: Multivariate analysis

Multivariate analysis looks at interactions among multiple variables.

Planned techniques:

- Correlation heatmap
- Pair plots for selected features
- Feature importance from a baseline tree model
- Grouped statistics by region, season, and crop type

---

## 5. Expected Exploration Outputs

The exploration phase is expected to produce:

1. Summary statistics for all major agricultural features.
2. Visualisations showing feature distributions.
3. Correlation matrix showing relationships between variables.
4. Identification of important features for modelling.
5. Detection of class imbalance in crop categories.
6. Evidence of weather and soil effects on yield.
7. Initial recommendations for feature selection.
8. Business interpretation of agricultural patterns.

---

## 6. Tools Used

| Tool | Purpose |
|---|---|
| Python | Main analysis language |
| pandas | Data manipulation |
| NumPy | Numerical calculations |
| matplotlib | Basic visualisation |
| seaborn | Statistical visualisation |
| scikit-learn | Baseline feature importance and modelling |

---

## 7. Connection to Week 2

This exploration plan builds directly on the Week 2 data preparation pipeline.

Week 2 produced:

- Cleaned agricultural records
- Treated missing values
- Removed duplicates
- Corrected unrealistic soil and weather values
- Scaled numerical features
- Encoded categorical variables
- Prepared a structured dataset

Week 3 uses that prepared dataset to explore patterns and select suitable models.
