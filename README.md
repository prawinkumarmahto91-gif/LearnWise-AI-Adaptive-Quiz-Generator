# LearnWise AI — Adaptive Quiz Generator

## IBM SkillsBuild Applied AI/ML Virtual Internship Project

### Problem selected
**SDG 4 — Quality Education:** AI quiz generator based on student performance and learning gaps.

The IBM SkillsBuild project guidance includes an AI project idea for an **AI quiz generator based on student performance and learning gaps**, and gives the sample problem of adapting learning content based on student progress and comprehension.

### Solution
LearnWise AI is an educational ML prototype that:
1. stores student question attempts,
2. measures performance by topic/subtopic,
3. identifies learning gaps,
4. recommends a focused set of quiz questions,
5. supports a path toward personalized difficulty.

### Dataset
For the final project, use the **UCI MathE (Assessing Mathematics Learning in Higher Education)** dataset.

UCI reports:
- 9,546 answer records
- 833 questions
- 372 students
- 8 fields including Student ID, Country, Question ID, answer correctness, Question Level, Topic, Subtopic and Keywords.

Dataset page:
https://archive.ics.uci.edu/dataset/1031/dataset+for+assessing+mathematics+learning+in+higher+education

Citation:
Flamia Azevedo, B., Pacheco, M., Fernandes, F. P., & Pereira, A. (2024). Assessing Mathematics Learning in Higher Education. UCI Machine Learning Repository. DOI: 10.34620/dadosipb/PW3OWY.

### Technologies
- Python
- Pandas
- Scikit-learn
- Streamlit
- Joblib
- Matplotlib (for optional EDA)
- UCI MathE dataset

### Project structure
```
IBM_Applied_AI_ML_Internship_AI_Quiz_Generator/
├── app.py
├── requirements.txt
├── README.md
├── data/
│   ├── demo_student_attempts.csv
│   └── question_bank.csv
├── models/
├── src/
│   ├── data_loader.py
│   ├── learning_gap_engine.py
│   ├── quiz_generator.py
│   └── train_model.py
└── docs/
    ├── Concept_Note.docx
    ├── Lean_Canvas.pdf
    └── Final_Presentation.pptx
```

### Run the demo
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate

pip install -r requirements.txt
python src/train_model.py
streamlit run app.py
```

### Important
The included CSV is a **synthetic demo dataset** so the prototype can run immediately without downloading external data. Do not describe its demo metrics as results from the UCI dataset.

For the final internship submission, replace the demo data with the UCI MathE dataset and rerun the training/evaluation before claiming final model metrics.

### Future scope
- student-level sequence models,
- adaptive difficulty,
- a larger verified question bank,
- multilingual explanations,
- teacher dashboard,
- LLM-based question generation with safety/quality checks,
- deployment using Streamlit Community Cloud or another hosting platform.

## Important status note

This repository currently includes synthetic demo data for demonstrating the workflow. Do not report demo metrics as real-world results. Before final evaluation, download and use the UCI MathE dataset, document the dataset preparation, retrain the model, and capture genuine screenshots from the running application.
