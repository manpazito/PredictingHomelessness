# Predictive Modeling for Addressing Homelessness Across the United States

## Overview
This project aims to predict homelessness rates across the United States using data from the U.S. Department of Housing and Urban Development (HUD). By leveraging the 2011-2017 Point-in-Time (PIT) Counts dataset, which provides annual estimates of homelessness across U.S. regions, we seek to identify key factors contributing to homelessness and provide actionable insights to better allocate resources and address this pressing issue nationwide.

Our analysis also compares predictions with insights presented in HUD's publication, [Market Predictors of Homelessness](https://www.huduser.gov/portal/publications/Market-Predictors-of-Homelessness.html), to validate model accuracy and refine our predictive approaches.

---

## Data Sources
The primary dataset for this project is the [HUD Point-in-Time (PIT) Counts by Continuum of Care (CoC)](https://www.huduser.gov/portal/datasets/hpmd.html). This dataset includes:
- Annual estimates of homeless populations by region
- Demographic breakdowns (e.g., veterans, individuals with disabilities)
- Subpopulation data (e.g., families, individuals with mental illness)
- Socioeconomic factors: unemployment rate, housing cost, poverty rate, and average salary
- Environmental data: temperature, air quality index
- Community resources: welfare office count, number of shelters
- Demographic factors: high school graduation rates, veteran status, immigrant population

This data is sourced from various reputable organizations, including:
- HUD Point-in-Time (PIT) Counts and System Performance Measures
- NOAA nClimDiv and Climate at a Glance Systems
- Census Intercensal Population Estimates
- Census ACS 5-Year Estimates
- Institute for Health Metrics and Evaluation (IHME)
- University of Wisconsin County Health Rankings (CHR)
- The Dartmouth Atlas of Health Care
- BLS Local Area Unemployment Statistics (LAUS)
- Federal Housing Finance Agency
- Eviction Lab at Princeton University

The data integrates environmental, demographic, economic, and housing market variables to provide a comprehensive view of the factors influencing homelessness.

---

## Methodology

### 1. **Exploratory Data Analysis (EDA)**
- Visualize trends, correlations, and anomalies
- Identify key contributors to homelessness rates

### 2. **Supervised Learning Models**
- **Regression Models**: Linear Regression, CART (Classification and Regression Trees), Random Forests
- **Boosting Techniques**: Gradient Boosting to improve model accuracy by reducing bias and variance

### 3. **Model Evaluation**
- Use metrics such as MSE (Mean Squared Error) and MAE (Mean Absolute Error) for accuracy
- Evaluate models on testing sets

### 4. **Hyperparameter Tuning**
- Optimize models using Grid Search for parameters like:
  - Number of trees (Random Forests)
  - Learning rate (Boosting)
  - Maximum depth (CART)

### 5. **Comparison with HUD Findings**
Our predictions are compared against the insights published in HUD’s [Market Predictors of Homelessness](https://www.huduser.gov/portal/publications/Market-Predictors-of-Homelessness.html). This step evaluates the practical applicability of the model and highlights any discrepancies to refine our understanding of homelessness trends.

---

## Data Preprocessing

### Selected Features
The features were selected based on absolute linear correlations and categorized as follows:

- **Climate Features**: Factors related to weather and environment
- **Demographic Features**: Population characteristics, including race, gender, and education
- **Economic Features**: Metrics such as poverty rates, income levels, and unemployment
- **Housing Features**: Data on rental rates, vacancy rates, and housing costs
- **Local Policies Features**: Policies affecting homelessness, such as shelters and public funding
- **Safety Net Features**: Support systems like federal funding and welfare programs

### Additional Features for Forecasting
- State identifier (`state_abr`)
- Year (`year`)

### Handling Missing Data
Missing data points were filled with zeros or categorical imputations where appropriate.

---

## Models Implemented

### Model 1: Linear Regression
- Achieved moderate accuracy with R² = 0.624 (Test)
- Residuals showed non-linear patterns, indicating possible underfitting

### Model 2: Regression Tree
- Improved R² = 0.749 (Test)
- Overfitted on training data (R² = 1.0)

### Model 3: Cross-Validated Regression Tree
- Tuned hyperparameters with Grid Search
- Achieved balanced performance: R² = 0.633 (Test)

### Model 4: Random Forest
- Best overall performance: R² = 0.819 (Test)
- Robust against overfitting with effective ensemble learning

### Model 5: Gradient Boosting
- Competitive performance: R² = 0.803 (Test)
- Effective at capturing non-linear relationships

---

## Residual Analysis
- Residuals were visualized for all models to assess distribution and variance.
- Random Forest and Gradient Boosting exhibited the most consistent residual patterns.

---

## Bootstrap Aggregation
Bootstrap sampling was performed to validate residual distributions and model robustness. Overlaid histograms of residuals highlighted the stability of Random Forest and Gradient Boosting models.

---

## Contributors
- Michelle Lee
- Emily Moberly
- Alyssa Hara
- Valeria Zheng
- Manuel Martinez Garcia

