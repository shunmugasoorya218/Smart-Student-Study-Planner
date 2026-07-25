import streamlit as st
from database.db import get_subjects
from logic.scheduler import generate_schedule
import pandas as pd

st.title("📅 Smart Schedule")

if "student_id" not in st.session_state:
    st.warning("Please login first!")
else:
    subjects = get_subjects(st.session_state.student_id)

    if subjects:
        schedule = generate_schedule(subjects, st.session_state.study_hours)

        df = pd.DataFrame(schedule, columns=["Subject", "Level", "Hours Per Day"])
        st.dataframe(df)

        st.bar_chart(df.set_index("Subject")["Hours Per Day"])
    else:
        st.warning("Add subjects first!")
