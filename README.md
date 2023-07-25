# Bankruptcy Prediction Model

## Project Overview

The Bankruptcy Prediction Model is a data-driven project aimed at predicting whether a company is at risk of bankruptcy or not. Bankruptcy prediction is a crucial task for financial institutions, investors, and creditors to assess the creditworthiness and financial health of a company before making any decisions related to loans, investments, or business partnerships.

In this project, we use a dataset containing financial features of various companies over multiple years. The dataset is divided into five separate files, each representing one year's financial data. Our main objective is to develop a robust bankruptcy prediction model that can accurately classify companies into two categories: "Bankrupt" and "Not Bankrupt."

## Project Workflow

1. **Data Collection**: The first step is to gather the necessary data for model development. The dataset files (`1year.arff`, `2year.arff`, `3year.arff`, `4year.arff`, and `5year.arff`) are obtained and loaded into the project.

2. **Data Preprocessing**: Before building the predictive model, we need to preprocess the data to make it suitable for training. This step involves handling missing values, converting data types, and any necessary data transformations.

3. **Missing Data Analysis**: We perform an analysis of missing data to understand the extent of missing values in each dataset. This helps us decide on the appropriate data imputation strategy.

4. **Data Imputation**: Since missing data can adversely affect the model's performance, we apply data imputation techniques to fill in the missing values. Two common imputation methods, Mean Imputation and k-Nearest Neighbors (k-NN) Imputation, are used in this project.

5. **Data Oversampling**: The dataset may suffer from class imbalance, where the number of instances in one class (e.g., "Bankrupt") is significantly lower than the other class ("Not Bankrupt"). To address this issue, we employ the Synthetic Minority Over-sampling Technique (SMOTE) to oversample the minority class and balance the dataset.

6. **Model Building and Evaluation**: With the preprocessed and balanced data, we proceed to build the bankruptcy prediction model. We explore several classifiers, including Gaussian Naive Bayes, Logistic Regression, Decision Tree, Random Forest, and Extreme Gradient Boosting (XGB) Classifier. Each model's performance is evaluated using cross-validation to ensure its effectiveness and generalizability.

7. **Web Application**: In addition to the notebook-based analysis, we create a user-friendly web application using Streamlit. The web app allows users to interact with the trained bankruptcy prediction model and make real-time predictions for a company's bankruptcy risk.

## Contact Information

- Model Developed by: Karan Singh Thakur, Ridhhi Aggarwal
- Email: kthakur1_be20@thapar.edu, raggarwal1_be20@thapar.edu

For any queries or feedback, please feel free to reach out to us!

---
This project aims to provide an effective and accessible tool for bankruptcy prediction, offering valuable insights to financial professionals and stakeholders. By combining data analysis, machine learning, and interactive web app development, we strive to make the bankruptcy prediction process more efficient and reliable.
