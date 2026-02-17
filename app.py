import streamlit as st
import pandas as pd
import string
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

nltk.download('stopwords')

# Load dataset
url = "https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv"
df = pd.read_csv(url, sep='\t', names=["label", "message"])
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# Preprocess function
def preprocess(text):
    text = text.lower()
    text = "".join([char for char in text if char not in string.punctuation])
    words = text.split()
    words = [word for word in words if word not in stopwords.words('english')]
    return " ".join(words)

df['clean_message'] = df['message'].apply(preprocess)

# TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['clean_message'])
y = df['label']

# Train model
model = MultinomialNB()
model.fit(X, y)

# UI
st.title("📩 SMS Spam Detection App")

user_input = st.text_area("Enter your message:")

if st.button("Predict"):
    cleaned = preprocess(user_input)
    vector_input = vectorizer.transform([cleaned])
    prediction = model.predict(vector_input)

    if prediction[0] == 1:
        st.error("🚨 This message is SPAM")
    else:
        st.success("✅ This message is HAM (Not Spam)")

