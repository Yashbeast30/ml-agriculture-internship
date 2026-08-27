# Week 3: Algorithm Selection and Rationale

## 1. Modelling Objectives

Two machine learning tasks are selected for this agricultural analysis project.

### Task 1: Crop Suitability Classification

The goal is to predict the most suitable crop based on soil and weather conditions.

- Input features: nitrogen, phosphorus, potassium, pH, rainfall, temperature, humidity
- Target variable: crop type
- Problem type: multiclass classification

### Task 2: Crop Yield Prediction

The goal is to predict crop yield using agricultural and environmental features.

- Input features: soil nutrients, rainfall, temperature, humidity, region, season
- Target variable: yield in tonnes per hectare
- Problem type: regression

---

## 2. Algorithm Selection Overview

| Task | Selected Algorithms | Reason |
|---|---|---|
| Classification | Logistic Regression | Simple baseline model |
| Classification | Random Forest Classifier | Handles non-linear agricultural relationships |
| Classification | Gradient Boosting Classifier | Strong performance on structured data |
| Regression | Linear Regression | Simple interpretable baseline |
| Regression | Random Forest Regressor | Captures complex interactions |
| Regression | XGBoost Regressor | Strong tabular data performance |

---

## 3. Rationale for Algorithm Selection

Agricultural data often contains non-linear relationships, thresholds, and interactions. For example, crop yield may increase with rainfall up to a point, but too much rainfall can reduce productivity. Similarly, soil nutrients may improve yield only within certain ranges.

Because of this, tree-based models such as Random Forest and Gradient Boosting are suitable.

---

## 4. Why Random Forest Was Selected

Random Forest was selected as the main model for both classification and regression.

### Reasons

1. It works well with tabular agricultural data.
2. It handles non-linear relationships.
3. It captures interactions between soil, weather, and crop features.
4. It is less sensitive to outliers than linear models.
5. It provides feature importance scores.
6. It is easy to interpret for business users.
7. It performs well without extremely large datasets.

---

## 5. Why Linear and Logistic Regression Were Used

Linear Regression and Logistic Regression were used as baseline models.

### Reasons

1. They are simple and fast.
2. They provide interpretable coefficients.
3. They help compare simple models against complex models.
4. They are useful for understanding linear relationships.
5. They provide a performance benchmark.

---

## 6. Modelling Pipeline Diagram

```text
Prepared Agricultural Dataset
            |
            v
Exploratory Data Analysis
            |
            v
Feature Selection
            |
            v
Train and Test Split
            |
            v
Preprocessing and Scaling
            |
            v
Model Training
            |
            v
Model Evaluation
            |
            v
Feature Importance Analysis
            |
            v
Business Insights and Recommendations
