# Challenges Encountered and Proposed Solutions

During the data acquisition and preparation simulation, several real-world agribusiness data challenges were encountered. This document details these challenges and the solutions implemented to overcome them.

## Challenge 1: Temporal Granularity Mismatch
**The Issue:** The primary soil dataset contained point-in-time measurements, the NASA weather data was daily, and the FAOSTAT yield data was annual. Merging these directly resulted in massive duplication and misaligned timelines.
**The Solution:** Aggregated the daily weather data into "Growing Season" metrics. For example, instead of using daily rainfall, I calculated the *Cumulative Rainfall during the 90-day germination and vegetative growth phase*. This aligned the weather features temporally with the annual yield harvest data.

## Challenge 2: The "Modifiable Areal Unit Problem" (MAUP)
**The Issue:** When merging regional FAOSTAT data with plot-level data, aggregating yields by large administrative regions masked local micro-climate variations, potentially leading to weak model performance.
**The Solution:** Introduced spatial clustering. Instead of using broad regional names, I used K-Means clustering on the soil and weather features to create "Agro-Ecological Zones" (AEZs). This created a new categorical feature that grouped similar micro-climates together, regardless of their administrative borders, providing a much stronger signal for the ML models.

## Challenge 3: Data Leakage in Weather Imputation
**The Issue:** When using KNN to impute missing rainfall data, there was a risk of using future weather data to impute past missing data, which would cause data leakage in a time-series forecasting context.
**The Solution:** Configured the KNN imputer to only look at spatial neighbors (plots in the same agro-ecological zone) and strictly historical data (previous 5 years) to fill gaps, ensuring the pipeline remains valid for real-world predictive deployment.

## Replicability Notes
To ensure this exact pipeline can be replicated by another analyst:
1. All random seeds for train/test splitting and imputation are fixed (`random_state=42`).
2. The exact versions of `pandas`, `scikit-learn`, and `numpy` are documented in the `requirements.txt` file.
3. The Python pipeline script (`data_preparation_pipeline.py`) is written using modular functions rather than a monolithic script, allowing step-by-step execution and debugging.
