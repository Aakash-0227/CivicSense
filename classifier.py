import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Read the dataset
data = pd.read_csv("dataset/complaint_dataset.csv")

# Store complaints
x = data["Complaint"]

# Store categories
y = data["Category"]

# Convert text into numbers
vectorizer = TfidfVectorizer()
x_vectorized = vectorizer.fit_transform(x)

# Train the model
model = MultinomialNB()
model.fit(x_vectorized, y)


def predict_category(complaint):

    new_complaint = [complaint]

    new_vector = vectorizer.transform(new_complaint)

    prediction = model.predict(new_vector)

    return prediction[0]






