import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import pickle

# Load dataset
data = pd.read_csv("dataset/lie_truth_dataset.csv")

X = data["text"]
y = data["label"]

# Build pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", MultinomialNB())
])

# Train model
model.fit(X, y)

# Save model
with open("lie_detector_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved!")