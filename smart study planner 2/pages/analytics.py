import streamlit as st
import pandas as pd
from database.db import get_subjects

st.title("📊 Analytics")

if "student_id" not in st.session_state:
    st.warning("Please login first!")
else:
    subjects = get_subjects(st.session_state.student_id)

    if not subjects:
        st.warning("No data to analyze")
    else:
        levels = [sub[1] for sub in subjects]

        df = pd.DataFrame(levels, columns=["Difficulty"])

        st.subheader("📈 Subject Difficulty Distribution")
        st.bar_chart(df["Difficulty"].value_counts())
