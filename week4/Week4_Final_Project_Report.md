# Week 4 Final Project Report: Machine Learning Data Analysis in Agriculture and Agribusiness

Prepared by: [Your Full Name]  
Role: Junior Machine Learning Data Analyst Intern  
Focus Area: Agriculture and Agribusiness  
Date: August 2026  
Week: 4 of 4  
Project Title: Machine Learning Data Analysis for Crop Productivity and Decision Support in Agriculture  

## Introduction

This final report presents the complete summary and evaluation of the four-week virtual internship project focused on machine learning data analysis in agriculture and agribusiness. The project was designed to simulate the full lifecycle of a data analysis project, starting from strategic planning and moving through data acquisition, data preparation, analysis, modelling, interpretation, and recommendation formulation. The main objective was to understand how agricultural data can be transformed into useful insights that support better decision-making for farmers, agribusinesses, advisors, and supply chain stakeholders.

The agricultural sector faces many challenges, including climate variability, soil degradation, water scarcity, input cost pressure, crop selection uncertainty, and market volatility. Traditional decision-making often depends on experience and observation, which remain valuable but can be strengthened with data-driven methods. Machine learning provides an opportunity to identify patterns in agricultural data that may not be immediately visible through manual analysis. This project explored that opportunity by focusing on crop suitability classification and crop yield prediction using structured agricultural data.

The project was intentionally scoped to be realistic for a junior machine learning data analyst internship. Instead of using complex satellite imaging or real-time sensor systems, the project focused on tabular agricultural data containing soil, weather, and crop-related variables. This approach allowed the project to demonstrate core machine learning skills such as problem definition, data cleaning, exploratory analysis, model selection, evaluation, and business interpretation. The final outcome is a structured analytical workflow supported by practical recommendations for agribusiness operations.

## Project Overview

The project was completed across four phases. Week 1 focused on strategic design and planning. Week 2 focused on data acquisition and preparation. Week 3 focused on execution of data analysis and modelling. Week 4 focused on project evaluation, reporting, and recommendation formulation. Each phase contributed to the final deliverable by building a stronger foundation for the next stage.

The strategic planning phase defined the problem, objectives, scope, methodology, key performance indicators, resources, constraints, and risks. The data acquisition phase identified publicly available agricultural data sources and explained how data quality issues should be assessed. The data preparation phase described the cleaning and transformation steps required to make the data suitable for analysis. The execution phase explored the data, selected algorithms, simulated model development, and interpreted results. This final report brings all these activities together and translates the technical outcomes into actionable recommendations.

## Strategic Planning Phase Summary

The first phase of the project established the direction of the entire internship. The problem statement focused on the gap between agricultural data availability and the ability to convert that data into useful decisions. Although agricultural data is increasingly available from weather stations, soil tests, satellite systems, farm records, and public statistics, many agribusinesses still lack accessible analytical tools that can turn this information into practical guidance.

The project objectives were defined around two main machine learning tasks. The first task was to predict or classify crop suitability based on soil and weather conditions. The second task was to estimate crop yield using agricultural features such as rainfall, temperature, humidity, soil pH, and nutrient levels. These objectives were selected because they are directly relevant to farm planning, input management, advisory services, procurement, and risk assessment.

The methodology adopted for the project was based on a structured data science framework similar to CRISP-DM. This framework includes business understanding, data understanding, data preparation, modelling, evaluation, and reporting. This approach ensured that the project did not jump directly into modelling without first understanding the agricultural context and data limitations. Key performance indicators were also defined, including data quality targets, model performance thresholds, feature importance interpretation, and the production of a stakeholder-ready report.

The planning phase also identified important constraints and risks. The main constraints included the four-week timeline, reliance on publicly available data, absence of field data collection, and the use of a simulated analysis environment. The main risks included poor data quality, class imbalance, model underperformance, scope creep, and limited regional representation. Mitigation strategies included selecting backup datasets, applying careful data cleaning, using multiple algorithms, documenting assumptions, and maintaining a clear project scope.

## Data Acquisition Phase Summary

The data acquisition phase focused on identifying suitable publicly available agricultural datasets. The selected data sources were chosen based on relevance to agriculture, public availability, structured format, sufficient record count, and agronomic interpretability. The primary dataset concept was based on crop recommendation and soil health data containing features such as nitrogen, phosphorus, potassium, soil pH, rainfall, temperature, humidity, and crop type. Secondary data concepts included agricultural yield statistics and weather or climate data.

The acquisition strategy recognised that agricultural data is often fragmented across different sources. Soil data may come from lab tests or open soil databases, weather data may come from climate services, and production data may come from national agricultural statistics. Therefore, the project documented the importance of aligning data by location, season, crop type, and measurement unit before analysis.

The data selection criteria were important because not all agricultural datasets are suitable for machine learning. Some datasets may be too aggregated, while others may lack the necessary features or contain too many missing values. For this project, tabular data was preferred because it is suitable for supervised learning and easier to analyse within the internship timeframe. The selected data themes were directly connected to agribusiness challenges such as crop selection, soil fertility, water availability, and productivity estimation.

## Data Preparation Phase Summary

The data preparation phase documented the process of transforming raw agricultural data into a clean and structured format. This phase was critical because machine learning models are highly sensitive to poor data quality. Agricultural datasets often contain missing values, inconsistent units, duplicate records, unrealistic sensor readings, and categorical inconsistencies.

The cleaning process began with error checking. Column names were standardised, categorical values were cleaned, and impossible agricultural values were corrected. For example, soil pH values were restricted to realistic agricultural ranges, negative yield values were reviewed, and rainfall outliers were capped based on reasonable thresholds. These corrections were based on domain knowledge rather than purely statistical rules, which is important in agricultural analysis.

Missing values were handled according to the nature of each feature. Soil-related features such as pH and nutrients were treated using robust imputation methods such as median imputation. Weather-related features such as rainfall and humidity were considered suitable for neighbour-based or region-based imputation because weather patterns often have spatial and seasonal relationships. Missing target values were not imputed because doing so could introduce bias and reduce the reliability of supervised learning.

Outlier treatment was also performed with agricultural context in mind. Some outliers represent data entry errors, while others may represent extreme but real agricultural events. Therefore, outliers were not removed blindly. Instead, they were reviewed and treated based on agronomic plausibility. Normalisation and scaling were applied to numerical features so that variables with larger ranges would not dominate model training. Categorical features were encoded into numerical format to prepare the dataset for machine learning algorithms.

Feature engineering was used to create more meaningful agricultural variables. Examples included nutrient balance ratios, thermal stress indicators, water availability indicators, and seasonal rainfall totals. These engineered features were designed to reflect real agricultural conditions more accurately than raw values alone. The final output of the data preparation phase was a structured dataset ready for exploratory analysis and modelling.

## Data Analysis and Modeling Phase Summary

The analysis and modelling phase began with exploratory data analysis. The purpose of this exploration was to understand distributions, detect relationships, evaluate class balance, and identify features that may be important for modelling. Visualisation techniques such as histograms, box plots, scatter plots, correlation heatmaps, and grouped summaries were used to examine the prepared dataset.

The exploratory analysis showed that agricultural productivity is influenced by multiple interacting factors. Rainfall was strongly associated with yield, indicating that water availability is a major driver of crop performance. Nitrogen was also highly important, reflecting its role in plant growth and soil fertility. Temperature showed a non-linear relationship with yield, suggesting that moderate conditions are beneficial while extreme heat can reduce productivity. Soil pH was more strongly linked to crop suitability than to yield, which suggests that pH is especially useful for crop selection decisions.

Two modelling tasks were executed. The classification task predicted crop suitability based on soil and weather features. The regression task predicted crop yield in tonnes per hectare. Logistic Regression and Linear Regression were used as baseline models, while Random Forest models were used as the main algorithms due to their ability to handle non-linear relationships and feature interactions. Gradient Boosting and XGBoost were also considered as alternative algorithms for structured data.

The simulated classification results showed that Random Forest Classifier achieved an accuracy of approximately 87 percent and a macro F1 score of approximately 0.84. The baseline Logistic Regression model achieved lower performance, with an accuracy of approximately 79 percent. The simulated regression results showed that Random Forest Regressor achieved an R-squared value of approximately 0.81, a mean absolute error of approximately 0.42 tonnes per hectare, and a mean absolute percentage error of approximately 12.4 percent. The Linear Regression baseline produced lower performance, showing that non-linear models are more suitable for this type of agricultural data.

Feature importance analysis showed that rainfall, nitrogen, temperature, soil pH, and humidity were among the most influential variables. These results are practically meaningful because they align with agricultural knowledge. Water availability, nutrient management, temperature stress, and soil conditions are central to crop growth. The model outputs therefore provide a useful foundation for decision support in agribusiness operations.

## Methodology Evaluation

The methodology used in this project was effective because it followed a clear and logical sequence. Starting with strategic planning ensured that the project had a defined problem, measurable objectives, and realistic scope. Moving into data acquisition and preparation ensured that the analysis was based on documented and structured data. The modelling phase then used the prepared dataset to generate insights in a controlled and interpretable way.

One strength of the methodology was its emphasis on domain relevance. Agricultural data cannot be analysed purely as numbers because the variables represent real biological, environmental, and operational processes. By applying agronomic reasoning during data cleaning and interpretation, the project produced insights that are more likely to be useful in practice. Another strength was the use of baseline models before advanced models. This allowed the project to measure whether more complex algorithms provided meaningful improvement.

A limitation of the methodology was the simulated nature of the results. Since the project was completed as part of a virtual internship, the modelling results were hypothetical and based on structured assumptions. However, the simulation was realistic and followed standard machine learning practices. Another limitation was the absence of real-time farm validation. Future work would require testing the models on actual farm records and receiving feedback from agricultural experts.

## Key Findings

The project produced several important findings. The first finding is that rainfall is one of the strongest predictors of crop yield. This confirms that water availability is central to agricultural productivity. Regions with unreliable rainfall may benefit from irrigation planning, drought monitoring, and seasonal forecasting. Agribusinesses can use this insight to prioritise water management strategies and advise farmers on risk reduction.

The second finding is that nitrogen availability is highly influential for both crop suitability and yield prediction. This highlights the importance of soil fertility management. However, the analysis also suggests that nutrient management should not focus on a single nutrient. Balanced nutrition involving nitrogen, phosphorus, potassium, and soil pH is more likely to support stable productivity.

The third finding is that soil pH is particularly useful for crop selection. Different crops have different pH preferences, and soil pH can affect nutrient availability. Therefore, soil testing can help farmers avoid planting crops that are poorly suited to their soil conditions. This can reduce input waste and improve the likelihood of successful harvests.

The fourth finding is that temperature has a non-linear relationship with productivity. Moderate temperatures support crop growth, but extreme heat can reduce yield. This finding is important because climate variability is increasing in many agricultural regions. Heat stress indicators can be combined with rainfall and humidity data to identify high-risk periods and guide preventive actions.

The fifth finding is that machine learning models can provide useful decision support, but they must be interpreted carefully. The Random Forest models performed well in simulation, but their recommendations should be reviewed by agricultural professionals before being applied in real operations. Model outputs should support human judgment rather than replace it.

## Key Insights for Agribusiness Decision-Making

The insights from this project can support several areas of agribusiness decision-making. At the farm level, the model can support crop selection by identifying which crops are more suitable for specific soil and weather conditions. This can help farmers reduce planting risk and improve resource allocation. It can also support fertiliser planning by highlighting the importance of nitrogen and nutrient balance.

At the advisory level, agricultural extension services can use similar models to provide personalised recommendations to farmers. Instead of giving broad regional advice, advisors can use soil test results and weather data to provide more specific guidance. This can improve the effectiveness of advisory services and increase farmer trust in data-driven recommendations.

At the supply chain level, yield prediction can support procurement planning, storage planning, transport scheduling, and market forecasting. If yield is expected to be lower than normal, agribusinesses can prepare alternative sourcing strategies. If yield is expected to be higher, logistics and storage capacity can be arranged in advance. This can reduce losses and improve operational efficiency.

At the risk management level, the model can support insurance, credit, and financial planning. Yield forecasts can help identify regions or farms that may face higher production risk. This can support early intervention, such as input support, irrigation assistance, or adjusted loan terms. The model can also help monitor the impact of weather stress over time.

## Recommendations

The first recommendation is to develop a crop recommendation decision-support tool based on the classification model. This tool could allow farmers or advisors to input soil test values and weather information, then receive a list of suitable crops along with confidence levels. The tool should include explanations for why certain crops are recommended, such as favourable pH, adequate rainfall, or suitable nutrient levels. This would make the system more transparent and practical.

The second recommendation is to implement soil testing and nutrient monitoring programmes. Since nitrogen and nutrient balance were important in the analysis, agribusinesses should encourage regular soil testing. Soil test results can be used to create targeted fertiliser recommendations rather than uniform application plans. This can reduce cost, improve productivity, and limit environmental damage caused by excessive fertiliser use.

The third recommendation is to improve water management planning. Because rainfall was the most influential feature in yield prediction, agribusinesses should invest in rainfall monitoring, seasonal forecasting, and irrigation scheduling. In regions with unstable rainfall, drought-tolerant crops or supplementary irrigation strategies may be recommended. In regions with excessive rainfall, drainage planning and disease monitoring may be important.

The fourth recommendation is to use yield forecasts for operational planning. Agribusinesses should integrate predictive yield estimates into procurement, logistics, storage, and financial planning. This can help organisations respond earlier to expected shortages or surpluses. Yield forecasts can also support contract planning and market risk management.

The fifth recommendation is to validate the model with real farm data before full deployment. The current project used simulated results and publicly available data concepts. To move into production, the model should be tested on actual farm records from different regions and seasons. Feedback from farmers and agronomists should be used to improve the model and ensure that recommendations are practical.

The sixth recommendation is to monitor model performance over time. Agricultural systems change due to climate patterns, soil health, farming practices, and crop varieties. A model trained on historical data may become less accurate if conditions change. Therefore, regular retraining and performance monitoring should be part of the deployment strategy.

The seventh recommendation is to build a simple dashboard for non-technical users. The dashboard could display predicted yield, crop suitability, important risk factors, regional comparisons, and soil nutrient status. Visual explanations should be used so that agricultural users can understand the results without needing technical machine learning knowledge. The dashboard could also allow users to compare different scenarios, such as changes in rainfall or fertiliser use.

## Real-World Implications

The real-world implications of this project are significant for agriculture and agribusiness. If applied responsibly, machine learning can improve productivity, reduce input waste, and support more resilient farming systems. Crop suitability recommendations can help farmers plant crops that are better matched to their environment, which can improve harvest stability. Yield prediction can help agribusinesses plan operations more effectively and reduce uncertainty.

The project also supports sustainability goals. Better fertiliser recommendations can reduce excess nutrient application, which can lower costs and limit environmental pollution. Improved water management can help conserve water resources and reduce drought risk. More accurate crop planning can reduce post-harvest losses by aligning production with storage and market capacity.

However, the project also highlights the need for responsible use of machine learning. Agricultural models should not be deployed without validation, local testing, and expert review. Recommendations must consider local farming practices, economic constraints, cultural preferences, and environmental conditions. A model may suggest an optimal crop, but the final decision should also consider market access, labour availability, input costs, and farmer experience.

## Limitations

The project has several limitations. The first limitation is that the results were simulated rather than validated on live farm data. This means that the performance metrics should be treated as indicative rather than definitive. The second limitation is that the dataset scope was limited to structured tabular data. It did not include satellite imagery, drone data, real-time sensor data, or detailed pest and disease records.

The third limitation is regional representation. Agricultural patterns vary strongly by location, soil type, climate zone, and farming practice. A model trained on one region may not perform well in another region without retraining or local calibration. The fourth limitation is temporal uncertainty. Weather patterns and climate conditions change over time, so historical relationships may not always remain stable.

The fifth limitation is related to data quality. Public agricultural datasets may contain missing values, inconsistent measurements, or reporting delays. Although the project documented strong data preparation methods, real-world deployment would require continuous data quality monitoring. These limitations do not reduce the value of the project as an internship simulation, but they should be considered before operational deployment.

## Future Work

Future work should focus on validating the model using real agricultural data from multiple regions and seasons. The dataset should be expanded to include more crops, more soil types, and more weather conditions. Additional features such as irrigation type, planting date, fertiliser application rate, pest pressure, and market price could improve the practical value of the model.

Another future direction is time-series forecasting. Instead of predicting a single annual yield, the model could be extended to forecast yield at different stages of the growing season using updated weather data. This would make the system more useful for in-season decision-making. Satellite vegetation indices could also be added to improve yield estimation for larger regions.

A further area for future work is explainability. Agricultural users are more likely to trust a model if they can understand why it makes a particular recommendation. Explainability tools such as feature importance, partial dependence plots, and simple explanation panels can be integrated into a dashboard. This would improve transparency and user confidence.

Finally, the project could be extended into a pilot deployment with a small group of farms or agribusiness advisors. The pilot would allow the model to be tested in real conditions, gather user feedback, and measure practical impact. After successful pilot testing, the system could be scaled to more regions and users.

## Intern Learning Journey

This internship provided practical exposure to the full lifecycle of a machine learning data analysis project in agriculture. The learning journey began with strategic planning, where the importance of problem definition, objectives, and success metrics became clear. It then moved into data acquisition and preparation, where the reality of messy agricultural data highlighted the importance of cleaning, validation, and domain knowledge.

The modelling phase demonstrated that algorithm selection should be based on the nature of the data and the business problem. It also showed that model evaluation is not only about technical metrics but also about whether the results can be interpreted and used in practice. The final reporting phase reinforced the importance of communication. A machine learning project is only valuable if its findings can be understood and applied by stakeholders.

The internship also developed critical thinking around data-driven decision-making. It showed that machine learning can support agriculture, but it cannot replace domain expertise. The best outcomes are likely to come from combining data science methods with agricultural knowledge, local experience, and responsible implementation.

## Conclusion

This final report completes the four-week virtual internship project on machine learning data analysis in agriculture and agribusiness. The project successfully covered strategic planning, data acquisition, data preparation, analysis, modelling, evaluation, and recommendation formulation. It demonstrated how structured agricultural data can be used to support crop suitability classification and yield prediction.

The simulated results showed that Random Forest models are suitable for the selected tasks because they can handle non-linear relationships and provide interpretable feature importance. Rainfall, nitrogen, temperature, soil pH, and humidity were identified as important variables with clear agricultural meaning. The insights generated by the project can support crop selection, fertiliser planning, irrigation management, procurement planning, and risk management.

The recommendations provided in this report are practical and feasible. They focus on decision support, soil testing, water management, yield forecasting, model validation, monitoring, and user-friendly reporting. By following these recommendations, agribusinesses can move from basic data analysis toward more informed, efficient, and sustainable decision-making.

The project concludes that machine learning has strong potential in agriculture when it is applied with clear objectives, careful data preparation, appropriate modelling, and domain-aware interpretation. The work completed during this internship provides a solid foundation for future agricultural analytics projects and demonstrates the value of data-driven decision support in agribusiness.
