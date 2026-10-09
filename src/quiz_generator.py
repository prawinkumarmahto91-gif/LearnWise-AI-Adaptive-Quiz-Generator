import pandas as pd

def generate_quiz(gaps, question_bank, n=5):
    if gaps.empty:
        pool = question_bank
    else:
        weak_topics = gaps["topic"].tolist()
        pool = question_bank[question_bank["topic"].isin(weak_topics)].copy()
        if pool.empty:
            pool = question_bank.copy()

    # Prefer basic questions first for remediation, then advanced.
    pool["difficulty_rank"] = pool["difficulty"].map({"Basic":0, "Advanced":1}).fillna(0)
    pool = pool.sort_values("difficulty_rank")
    return pool.drop(columns=["difficulty_rank"]).head(n)
