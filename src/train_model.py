import joblib
import pandas as pd
from pathlib import Path
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

DATA = Path("data/demo_student_attempts.csv")
MODEL = Path("models/answer_prediction_pipeline.joblib")

df = pd.read_csv(DATA)

# Text fields are combined so the baseline can learn from topic,
# subtopic, difficulty and keywords.
df["text"] = (
    df["Question Level"].astype(str) + " " +
    df["Topic"].astype(str) + " " +
    df["Subtopic"].astype(str) + " " +
    df["Keywords"].astype(str)
)

X_train, X_test, y_train, y_test = train_test_split(
    df["text"], df["Type of Answer"],
    test_size=0.20, random_state=42, stratify=df["Type of Answer"]
)

model = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1,2), min_df=1)),
    ("clf", LogisticRegression(max_iter=1000, random_state=42))
])

model.fit(X_train, y_train)
pred = model.predict(X_test)

print("Accuracy:", round(accuracy_score(y_test, pred), 4))
print("F1:", round(f1_score(y_test, pred), 4))
print(classification_report(y_test, pred))

MODEL.parent.mkdir(exist_ok=True)
joblib.dump(model, MODEL)
print(f"Saved model to {MODEL}")
