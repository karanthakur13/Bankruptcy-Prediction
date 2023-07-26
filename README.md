# Bankruptcy Prediction Model

## Project Overview

The Bankruptcy Prediction Model is a data-driven project aimed at predicting whether a company is at risk of bankruptcy or not. Bankruptcy prediction is a crucial task for financial institutions, investors, and creditors to assess the creditworthiness and financial health of a company before making any decisions related to loans, investments, or business partnerships.

The project revolves around a dataset containing financial features of various companies over multiple years. Each observation in the dataset corresponds to a specific company's financial information for a particular year. The dataset is divided into five separate files, each representing one year's financial data. Our main objective is to develop a robust bankruptcy prediction model that can accurately classify companies into two categories: "Bankrupt" and "Not Bankrupt."

## Project Workflow

1. **Data Collection**: The initial step is to gather the necessary data for model development. The dataset files (`1year.arff`, `2year.arff`, `3year.arff`, `4year.arff`, and `5year.arff`) are obtained and loaded into the project. These files are in the Attribute-Relation File Format (ARFF), which is commonly used for representing data with attributes and instances.

2. **Data Preprocessing**: Before building the predictive model, we need to preprocess the data to make it suitable for training. This step involves handling missing values, converting data types, and any necessary data transformations. Additionally, we will combine the five separate datasets into a single cohesive dataset for analysis.

3. **Missing Data Analysis**: In real-world datasets, missing data is a common occurrence. It can occur due to various reasons like data collection errors or incomplete records. We perform an analysis of missing data to understand the extent of missing values in each dataset. This helps us decide on the appropriate data imputation strategy.

4. **Data Imputation**: Since missing data can adversely affect the model's performance, we apply data imputation techniques to fill in the missing values. Two common imputation methods, Mean Imputation and k-Nearest Neighbors (k-NN) Imputation, are used in this project. Mean imputation replaces missing values with the mean of the available data for that feature, while k-NN imputation predicts missing values based on the values of k-nearest neighbors.

5. **Data Oversampling**: In many classification problems, including bankruptcy prediction, the dataset may suffer from class imbalance. Class imbalance occurs when the number of instances in one class (e.g., "Bankrupt") is significantly lower than the other class ("Not Bankrupt"). This can lead the model to be biased towards the majority class and perform poorly in predicting the minority class. To address this issue, we employ the Synthetic Minority Over-sampling Technique (SMOTE). SMOTE generates synthetic samples of the minority class by interpolating between existing instances, thus creating a balanced dataset.

6. **Feature Selection**: Not all the features in the dataset may contribute equally to the bankruptcy prediction task. Some features may have a more significant impact, while others may be irrelevant or even detrimental to the model's performance. We perform feature selection techniques such as correlation analysis and feature importance ranking to select the most relevant features for model training.

7. **Model Building and Evaluation**: With the preprocessed, balanced, and feature-selected data, we proceed to build the bankruptcy prediction model. We explore several classifiers, including Gaussian Naive Bayes, Logistic Regression, Decision Tree, Random Forest, and Extreme Gradient Boosting (XGB) Classifier. Each model's performance is evaluated using appropriate metrics like accuracy, precision, recall, F1 score, and ROC-AUC score through cross-validation to ensure its effectiveness and generalizability.

8. **Hyperparameter Tuning**: Many machine learning models have hyperparameters that influence their performance. We perform hyperparameter tuning using techniques like grid search or random search to find the optimal hyperparameters that yield the best model performance.

9. **Web Application**: In addition to the notebook-based analysis, we create a user-friendly web application using Streamlit. The web app allows users to interact with the trained bankruptcy prediction model and make real-time predictions for a company's bankruptcy risk. Users can input the financial features of a company, and the model will provide a prediction indicating whether the company is at risk of bankruptcy or not.

## Conclusion

This project aims to provide an effective and accessible tool for bankruptcy prediction, offering valuable insights to financial professionals and stakeholders. By combining data analysis, machine learning, and interactive web app development, we strive to make the bankruptcy prediction process more efficient and reliable. The model's predictions can assist financial institutions in making well-informed decisions regarding investments, loans, and partnerships, ultimately reducing the risks associated with bankruptcy.
