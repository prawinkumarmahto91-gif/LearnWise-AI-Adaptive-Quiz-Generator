import pandas as pd

UCI_URL = "https://archive.ics.uci.edu/dataset/1031/dataset+for+assessing+mathematics+learning+in+higher+education"

def load_local(path="data/demo_student_attempts.csv"):
    return pd.read_csv(path)

def normalize_columns(df):
    df = df.copy()
    rename = {
        "Student ID": "student_id",
        "Student Country": "student_country",
        "Question ID": "question_id",
        "Type of Answer": "correct",
        "Question Level": "question_level",
        "Topic": "topic",
        "Subtopic": "subtopic",
        "Keywords": "keywords",
    }
    df = df.rename(columns=rename)
    df["correct"] = df["correct"].astype(int)
    return df

def load_demo():
    return normalize_columns(load_local())
