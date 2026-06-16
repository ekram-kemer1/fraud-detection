Improved Detection of Fraud Cases for E-commerce and Bank Transactions
Project Overview

This project was completed as part of the 10 Academy Artificial Intelligence Mastery Program (Week 5 & 6 Challenge).

The objective is to develop machine learning models capable of detecting fraudulent transactions in both e-commerce and bank credit card datasets. Due to the highly imbalanced nature of fraud data, special attention was given to feature engineering, class imbalance handling, model evaluation, and explainability.
Business Problem

Fraudulent transactions result in significant financial losses and reputational damage for businesses. At the same time, incorrectly flagging legitimate transactions as fraudulent negatively affects customer experience.

The goal of this project is to build fraud detection models that:

Accurately identify fraudulent transactions
Minimize false positives
Support risk monitoring and decision-making
Provide explainable insights into fraud patterns
Datasets
1. Fraud_Data.csv

E-commerce transaction data containing:

User information
Device information
Purchase behavior
IP addresses
Fraud labels

Target Variable:
class

0 = Legitimate Transaction
1 = Fraudulent Transaction
2. IpAddress_to_Country.csv

Contains IP address ranges mapped to countries and is used for geolocation enrichment.

3. creditcard.csv

Bank credit card transactions with anonymized PCA-transformed features.

Target Variable:
Class

0 = Legitimate Transaction
1 = Fraudulent Transaction
Project Structure
fraud-detection/

├── .github/
│   └── workflows/
│       └── unittests.yml

├── data/
│   ├── raw/
│   └── processed/

├── notebooks/
│   ├── eda-fraud-data.ipynb
│   ├── eda-creditcard.ipynb
│   ├── feature-engineering.ipynb
│   ├── modeling.ipynb
│   └── shap-explainability.ipynb

├── src/
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   └── modeling.py

├── tests/
│   └── test_smoke.py

├── models/

├── requirements.txt

├── README.md

└── .gitignore
Data Cleaning and Preprocessing

The following preprocessing steps were performed:

Missing value analysis
Duplicate record detection and removal
Datetime conversion
Data type correction
Geolocation enrichment using IP-to-country mapping
Feature engineering
One-hot encoding of categorical variables
Numerical feature scaling
Exploratory Data Analysis

EDA was conducted on both datasets to understand:

Feature distributions
Transaction patterns
Fraud occurrence patterns
Country-level fraud distribution
Relationships between variables and fraud labels

Key findings:

Fraudulent transactions represent a minority class in both datasets.
Certain countries exhibit higher fraud rates.
Transaction timing and account age provide useful fraud indicators.
Device usage patterns contribute to fraud prediction.
Feature Engineering

Several new features were created:

Temporal Features
time_since_signup
hour_of_day
day_of_week
Behavioral Features
user_tx_count
device_tx_count
Geographical Features
country

These engineered features improve the model's ability to identify suspicious behavior.
Handling Class Imbalance

Both datasets exhibit significant class imbalance.

To address this issue:

Stratified Train-Test Split was used.
SMOTE (Synthetic Minority Oversampling Technique) was applied only to the training dataset.
The test dataset remained untouched to prevent data leakage.
Models Developed
Logistic Regression

Used as the baseline model due to its interpretability.

Random Forest

Used as the primary ensemble model because of its ability to capture complex fraud patterns.

Model Evaluation

The following metrics were used:

F1 Score
Average Precision Score (AUC-PR)
Confusion Matrix
Cross Validation

Logistic Regression
| Metric                  | Value  |
| ----------------------- | ------ |
| F1 Score                | 0.1590 |
| Average Precision Score | 0.0923 |

Random Forest
| Metric                  | Value  |
| ----------------------- | ------ |
| F1 Score                | 0.2272 |
| Average Precision Score | 0.1479 |


Cross Validation (Random Forest)
| Metric             | Value  |
| ------------------ | ------ |
| Mean F1 Score      | 0.7424 |
| Standard Deviation | 0.0023 |

Model Selection

Random Forest was selected as the final model because:

It achieved the highest F1 Score.
It achieved the highest Average Precision Score.
It significantly reduced false positives compared to Logistic Regression.
Cross-validation demonstrated stable performance.

## Task 3 — Model Explainability
- SHAP TreeExplainer applied to Random Forest (best model)
- Summary plots generated for both Fraud_Data and CreditCard datasets
- Force plots for True Positive, False Positive, and False Negative cases
- Top 5 fraud drivers identified with business recommendations
