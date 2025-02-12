import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import re
import string

data = pd.read_csv("data.csv")
emails = data['Email']
sentiments = data['Sentiment']

#print(emails.head(), categories.head())

def clean(text):
    text = text.replace("\n", " ").replace("\r", " ")
    text = " ".join(text.split())
    text = text.lower()
    text = re.sub(f"[{string.punctuation}]", "", text)
    text = re.sub(r"\d+", "", text)
    return text

emails = data['Email'].apply(clean)
X_train, X_test, y_train, y_test = train_test_split(emails, sentiments, test_size=0.3, random_state=42, stratify=sentiments)

vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

model = LogisticRegression()
model.fit(X_train_tfidf, y_train)

y_pred = model.predict(X_test_tfidf)

def categorize_email(text):
    text = clean(text)
    tfidf = vectorizer.transform([text])
    return model.predict(tfidf[0])

# print("Accuracy:", accuracy_score(y_test, y_pred))
# print("Classification Report:\n", classification_report(y_test, y_pred))

