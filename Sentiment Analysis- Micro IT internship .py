#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# sentiment_analysis_project.py

"""
Sentiment Analysis using Machine Learning
Author: Masini Anvitha
Description: This project analyzes the sentiment (positive, negative, neutral) of a given text input.
I used basic Natural Language Processing techniques and trained a Logistic Regression model
on a sample dataset. I also built a simple prediction interface for testing sentences.
"""

import nltk
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.feature_extraction.text import TfidfVectorizer

# Downloading the tokenizer from NLTK
nltk.download('punkt')

# 1. Sample data– a small custom dataset for demonstration
data = {
    'text': [
        "I love this phone, it's amazing!",
        "Worst experience ever. Totally disappointed.",
        "Not bad, but could be better.",
        "Absolutely fantastic service!",
        "I hate it. It's terrible.",
        "Okay product. Nothing special.",
        "Very happy with my purchase.",
        "Extremely poor performance.",
        "I feel good using it.",
        "The design is not impressive."
    ],
    'sentiment': [
        "positive", "negative", "neutral", "positive", "negative",
        "neutral", "positive", "negative", "positive", "neutral"
    ]
}

# 2. Load into DataFrame
df = pd.DataFrame(data)

# 3. Preprocessing: Vectorize using TF-IDF
tfidf = TfidfVectorizer()
X = tfidf.fit_transform(df['text'])
y = df['sentiment']

# 4. Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Model Training– Logistic Regression for its simplicity and good baseline performance
model = LogisticRegression()
model.fit(X_train, y_train)

# 6. Model Evaluation
y_pred = model.predict(X_test)
print("\n Model Evaluation")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# 7. Predict Function– to test live input
def predict_sentiment():
    print("\n Test Sentiment Prediction")
    while True:
        text = input("Enter a sentence (or type 'exit'): ")
        if text.lower() == 'exit':
            print("Exiting Sentiment Analysis.")
            break
        vec = tfidf.transform([text])
        prediction = model.predict(vec)[0]
        print(f"Sentiment: {prediction.upper()}")

# 8. Run the interface
if __name__ == "__main__":
    print("Sentiment Analyzer Ready")
    predict_sentiment()

    


# In[ ]:




