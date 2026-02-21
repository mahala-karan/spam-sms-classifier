# 📩 SMS Spam Detection Web App

A Machine Learning based SMS Spam Detection system that classifies messages as Spam or Ham (Not Spam) using Natural Language Processing and Naive Bayes algorithm.

## 📌 Problem Statement

Spam messages pose serious security risks including phishing attacks, fraud, and malware distribution. Manual filtering is inefficient. This project aims to build an automated SMS spam classifier using Machine Learning.

## 💡 Proposed Solution

The system uses:

- Natural Language Processing (NLP)
- TF-IDF Vectorization
- Multinomial Naive Bayes Classifier
- Streamlit Web Interface for deployment

The application allows users to input any SMS message and instantly receive a Spam/Ham prediction.

## ⚙️ Tech Stack

- Python
- Pandas
- Scikit-learn
- NLTK
- Streamlit

## 📊 Dataset

- SMS Spam Collection Dataset
- 5572 labeled SMS messages
- Labels:
  - `0` → Ham
  - `1` → Spam

## 🧠 Machine Learning Pipeline

1. Dataset Loading
2. Data Cleaning (Label Encoding)
3. Text Preprocessing
4. TF-IDF Feature Extraction
5. Model Training (Multinomial Naive Bayes)
6. Model Evaluation
7. Deployment using Streamlit

## 📈 Model Performance

- Accuracy: ~97%
- Evaluation Metrics:
  - Precision
  - Recall
  - F1-score
