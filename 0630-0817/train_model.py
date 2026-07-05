import numpy as np
import joblib
from sklearn.linear_model import LogisticRegression

# Small demo dataset (replace with real medical data later)
texts = [
    "severe chest pain and trouble breathing",
    "mild cough and sore throat",
    "high fever and body aches",
    "stomach pain and vomiting",
    "headache for three days",
    "slight runny nose",
    "bleeding from hand and turning blue",
]

severity_labels = ["CRITICAL", "LOW", "HIGH", "MEDIUM", "MEDIUM", "LOW", "HIGH"]
category_labels = [
    "Cardiac/Respiratory",
    "Respiratory/Minor",
    "Infectious",
    "Gastrointestinal",
    "Neurological",
    "General",
    "General",
]

def text_to_vec(text):
    tokens = text.lower().split()
    vec = np.zeros(100)
    for t in tokens:
        idx = hash(t) % 100
        vec[idx] += 1.0
    return vec

X = np.array([text_to_vec(t) for t in texts])
y_sev = np.array(severity_labels)
y_cat = np.array(category_labels)

severity_model = LogisticRegression(max_iter=1000)
category_model = LogisticRegression(max_iter=1000)

severity_model.fit(X, y_sev)
category_model.fit(X, y_cat)

joblib.dump(severity_model, "severity_model.pkl")
joblib.dump(category_model, "category_model.pkl")

print("Demo severity and category models trained and saved.")
