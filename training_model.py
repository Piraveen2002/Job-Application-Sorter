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
    text = re.sub(f"[{string.punctuation}]", "", text)  # Remove punctuation
    text = re.sub(r"\d+", "", text)  # Remove numbers
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

# temp = clean("Dear Piraveen, Thank you for applying for the Software Engineer position at Hola. We were impressed with your qualifications and would love the opportunity to speak with you further. We would like to invite you for an interview to discuss your experience and how you might contribute to our team. Below are the details: Date: February 2nd, 2025, Time: 3:00 PM, Location: Virtual Meeting Link, Interview Format: Virtual. Please let us know if the proposed time works for you, or if an alternative time is more convenient. If this is a virtual interview, we will share the meeting link and any necessary instructions prior to the interview. We look forward to speaking with you and learning more about your background. If you have any questions, feel free to reach out. Best regards, Amanda Raponi, HR Manager, Hola.")
# print(categorize_email(temp))

# print("Accuracy:", accuracy_score(y_test, y_pred))
# print("Classification Report:\n", classification_report(y_test, y_pred))

