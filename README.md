# Bankruptcy Prediction Model

This project implements a bankruptcy prediction model using various machine learning algorithms. The goal is to predict whether a company is at risk of bankruptcy based on financial indicators and other relevant features.

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Data](#data)
4. [Data Preprocessing](#data-preprocessing)
5. [Feature Selection](#feature-selection)
6. [Modeling](#modeling)
7. [Running the Model](#running-the-model)
8. [Contact](#contact)

## 1. Introduction <a name="introduction"></a>

In this project, we aim to predict bankruptcy risk for companies using various financial indicators. The model is built using a combination of different machine learning algorithms and is evaluated on different datasets spanning five years.

## 2. Installation <a name="installation"></a>

Before running the notebook, please ensure you have the required libraries installed. You can install them using the following commands:

```
!pip install fancyimpute
!pip install scikit-learn
!pip install impyute
!pip install missingno
!pip install imblearn
!pip install lightgbm
!pip install xgboost
!pip install streamlit
```

## 3. Data <a name="data"></a>

The data for this project consists of multiple `.arff` files, each representing the financial indicators of companies for a specific year. The data is loaded and organized into five pandas DataFrames corresponding to each year.

## 4. Data Preprocessing <a name="data-preprocessing"></a>

### 4.1 Missing Data Analysis
Missing data is analyzed, and rows with missing values are dropped from the dataset to ensure clean data for modeling.

### 4.2 Data Imputation
Missing values are imputed using two methods: mean imputation and k-Nearest Neighbors (k-NN) imputation. The imputed dataframes are then used for further analysis.

## 5. Feature Selection <a name="feature-selection"></a>

A feature selection technique, Recursive Feature Elimination (RFE), is applied to select the best features for the modeling process.

## 6. Modeling <a name="modeling"></a>

Several machine learning classifiers are used for bankruptcy prediction. The following classifiers are used:
- Gaussian Naive Bayes
- Logistic Regression
- Decision Tree
- Random Forest
- Extreme Gradient Boosting (XGBoost)

The models are evaluated using k-fold cross-validation and metrics such as Accuracy, Precision, and Recall.

## 7. Running the Model <a name="running-the-model"></a>

To run the bankruptcy prediction model, execute the Streamlit app. The app allows you to input the financial indicators for your company and get the prediction of bankruptcy risk.

## 8. Contact <a name="contact"></a>

For any questions or feedback related to this project, please feel free to contact the developers:
- Karan Singh Thakur: kthakur1_be20@thapar.edu
- Ridhhi Aggarwal: raggarwal1_be20@thapar.edu

Thank you for using the bankruptcy prediction model!
