# MavunoX_DS
## Description

Welcome to the Data Science component of the MavunoX project! This machine learning system is dedicated to predicting the harvest season by analyzing a myriad of environmental factors. MavunoX is a comprehensive initiative focused on leveraging technology for sustainable agriculture, and this Data Science module plays a crucial role in optimizing crop yield predictions.

The Data Science/ML Project makes use of 3 models
- Main Model
- Soil pH Predictor
- Water Availabity model

## Main Model Architeture 
# MavunoX Data Science Project

## Main Model Architecture and Data Analysis

### Data Overview
The dataset, sourced from the [Klusterthon Hackathon](https://www.kluster.africa/problem-statements/precision-farming-for-best-product-results-with-data), provides valuable insights into environmental factors influencing harvest seasons across four countries: Nigeria, South Africa,Kenya, and Sudan. Essential features include temperature, humidity, pH, water availability, crop type, and the target label - the harvest season.

### Data Analysis

Our preliminary analysis revealed several key observations:

- **Most Common Season:** The dataset predominantly consists of data from the rainy season.

- **Dominant Crop:** Maize emerged as the most frequently occurring crop in the distribution.

- **Regional Concentration:** The majority of the dataset originates from the Nigerian region, showcasing a notable geographical focus.

![Distribution Image 1](categorical_value_counts_emerald.png)


### Data Preprocessing

To prepare the data for model training, we executed the following preprocessing steps:

- **Dropping Unnecessary Columns:** The "harvest season" column was removed, as it is not needed, and "temperature" was excluded to prevent data leakage.

- **Feature Engineering:** We created a new variable, the "ph_to_water_availability_ratio," to capture additional insights.

- **One-Hot Encoding:** Categorical variables ('Country' and 'label') were one-hot encoded for compatibility with machine learning models.

### Model Training

The XGBoost classifier was employed to predict harvest seasons based on the provided features. The model training process involved label encoding the target variable ('season') and splitting the data into training and testing sets.

### Model Evaluation

The trained model demonstrated promising results on the test set:

- **Accuracy:** The model achieved an accuracy of 89%.

- **Precision, Recall, and F1-Score:**

    |       | Precision | Recall | F1-Score | Support |
    |-------|-----------|--------|----------|---------|
    | 0     | 0.85      | 0.90   | 0.88     | 117     |
    | 1     | 1.00      | 1.00   | 1.00     | 20      |
    | 2     | 1.00      | 1.00   | 1.00     | 62      |
    | 3     | 0.84      | 0.78   | 0.81     | 81      |

    - **Accuracy:** 89%
    - **Macro Avg Precision:** 92%
    - **Macro Avg Recall:** 92%
    - **Macro Avg F1-Score:** 92%

These results suggest that the model is effective in predicting harvest seasons based on environmental factors.

For a more in-depth analysis and visualizations, please refer to the associated [Notebook](mavanux-model-building.ipynb). If you have any questions or suggestions, feel free to reach out. Thank you for your interest in the MavunoX Data Science Project!

