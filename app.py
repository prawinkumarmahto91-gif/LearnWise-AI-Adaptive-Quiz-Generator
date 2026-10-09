import pandas as pd
import streamlit as st
from src.learning_gap_engine import top_gaps
from src.quiz_generator import generate_quiz
from src.data_loader import load_demo

st.set_page_config(page_title="LearnWise AI", page_icon="📚", layout="wide")
st.title("📚 LearnWise AI")
st.caption("Adaptive quiz recommendation prototype for identifying learning gaps.")

df = load_demo()
qb = pd.read_csv("data/question_bank.csv")

student_ids = sorted(df["student_id"].unique())
student_id = st.sidebar.selectbox("Select Student", student_ids)

gaps = top_gaps(df, student_id, 3)
c1, c2, c3 = st.columns(3)
c1.metric("Student Attempts", int((df.student_id == student_id).sum()))
c2.metric("Overall Accuracy", f"{df.loc[df.student_id == student_id, 'correct'].mean()*100:.1f}%")
c3.metric("Topics Needing Practice", len(gaps))

st.subheader("Learning Gaps")
if not gaps.empty:
    display = gaps.copy()
    display["accuracy"] = (display["accuracy"]*100).round(1).astype(str) + "%"
    display["gap_score"] = (display["gap_score"]*100).round(1).astype(str) + "%"
    st.dataframe(display, use_container_width=True)

st.subheader("Recommended Quiz")
quiz = generate_quiz(gaps, qb, n=5)
for i, row in quiz.reset_index(drop=True).iterrows():
    st.markdown(f"**{i+1}. [{row['topic']} / {row['subtopic']}]** {row['question']}")
    st.write(f"Difficulty: {row['difficulty']}")
    with st.expander("Show answer"):
        st.write(row["answer"])
        st.caption(row["explanation"])

st.info("Demo mode uses a generated sample interaction dataset. Replace it with the UCI MathE dataset for final evaluation.")
