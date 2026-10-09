import pandas as pd

def topic_gaps(df, student_id):
    student = df[df["student_id"] == student_id].copy()
    if student.empty:
        return pd.DataFrame(columns=["topic","attempts","accuracy","gap_score"])
    g = student.groupby("topic").agg(
        attempts=("correct","size"),
        accuracy=("correct","mean")
    ).reset_index()
    g["gap_score"] = 1 - g["accuracy"]
    return g.sort_values(["gap_score","attempts"], ascending=[False,False])

def top_gaps(df, student_id, n=3):
    return topic_gaps(df, student_id).head(n)
