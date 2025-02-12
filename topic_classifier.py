import pandas as pd
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import re
import string

data = pd.read_csv("Book1.csv")
emails = data['Email']
categories = data['Category']

def clean(text):
    text = text.replace("\n", " ").replace("\r", " ")
    text = " ".join(text.split())
    text = text.lower()
    text = re.sub(f"[{string.punctuation}]", "", text)  # Remove punctuation
    text = re.sub(r"\d+", "", text)  # Remove numbers
    return text

emails = emails.apply(clean)

X_train, X_test, y_train, y_test = train_test_split(emails, categories, test_size=0.2, random_state=101, stratify=categories)

tfidf = TfidfVectorizer()
X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)

model = LogisticRegression()
model.fit(X_train_tfidf, y_train)

y_pred = model.predict(X_test_tfidf)

def predict_category(text):
    text = clean(text)
    vector = tfidf.transform([text])
    return model.predict(vector[0])

# print("Accuracy:", accuracy_score(y_test, y_pred))
# print("Classification Report:\n", classification_report(y_test, y_pred))



