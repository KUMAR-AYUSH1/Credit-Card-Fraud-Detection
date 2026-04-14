# Credit-Card-Fraud-Detection
A complete end-to-end machine learning solution to detect fraudulent credit card transactions. This project features a highly accurate XGBoost backend served via FastAPI and an interactive user interface built with Streamlit.

After that containerized using Docker
You can run the entire stack immediately using Docker:
# Pull the image
docker pull kumar2700/fraud-detection:latest

# Run the containers (API on 8000, UI on 8501)
docker run -p 8000:8000 -p 8501:8501 kumar2700/fraud-detection

The project was developed in four distinct phases:
fraud_dataset_preprocess: Data cleaning, feature engineering .
test1: handling class imbalance and Initial benchmarking of various ML models.
test2: Stress-testing top-performing models against different data subsets.
test3: Final hyperparameter tuning and selection of the XGBoost model

🚀 Overview
Goal: Identify fraudulent transactions to prevent financial loss.
Model: After testing multiple algorithms (Logistic Regression, Random Forest, KNN, dt, etc.), XGBoost was selected as the final model due to its superior performance.
Performance:
Accuracy: 97%
Recall: 96% (Optimized to catch the maximum number of fraud cases)
Dataset url 
https://www.kaggle.com/datasets/kartik2112/fraud-detection?select=fraudTrain.csv


#requrement 
# Data Processing & Modeling
pandas
numpy
scikit-learn
xgboost
pickle

# Backend API
fastapi
uvicorn
pydantic

# Frontend UI
streamlit
requests
