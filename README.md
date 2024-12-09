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

## How to Use
Before running any code, execute the `Init.ipynb` file to set up the environment and initialize the project.

---

## Contributors
- Michelle Lee
- Emily Moberly
- Alyssa Hara
- Valeria Zheng
- Manuel Martinez Garcia
