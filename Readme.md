<img width="704" height="677" alt="Screenshot 2026-02-17 160310" src="https://github.com/user-attachments/assets/a72a767a-e1a7-4726-b264-9700625063ea" />
<img width="979" height="661" alt="Screenshot 2026-02-17 160254" src="https://github.com/user-attachments/assets/1f9e085a-b588-43ec-bafa-ac9ada1e7edb" />
<img width="1046" height="429" alt="Screenshot 2026-02-17 160238" src="https://github.com/user-attachments/assets/e7e543ee-e170-420f-87a0-2a794fbdae3b" />
<img width="722" height="319" alt="Screenshot 2026-02-17 160226" src="https://github.com/user-attachments/assets/55217ff3-3f3d-4ad4-a38c-dbef5727d9a0" />
<img width="966" height="699" alt="Screenshot 2026-02-17 160215" src="https://github.com/user-attachments/assets/e26e63d3-ba6d-49f3-9e3e-5932f9a72661" />
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

