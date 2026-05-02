import pandas as pd
import re
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

# Load
data = pd.read_csv("dataset.csv")
data = data.dropna()

# Clean text
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

data["email"] = data["email"].apply(clean_text)

X = data["email"]
y = data["label"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Vectorizer
vectorizer = TfidfVectorizer(
    stop_words="english",
    ngram_range=(1,2),
    min_df=2,
    max_df=0.95,
    max_features=8000
)

X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Model
model = LogisticRegression(
    class_weight="balanced",
    max_iter=2000
)

model.fit(X_train_vec, y_train)

# Evaluate
pred = model.predict(X_test_vec)

print("Accuracy:", accuracy_score(y_test, pred))
print(classification_report(y_test, pred))

# Save
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Saved")