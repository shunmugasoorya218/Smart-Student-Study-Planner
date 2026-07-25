import streamlit as st
from database.db import get_subjects
from logic.stress import calculate_stress
import datetime

st.title("📝 Exam Planner & Stress Analysis")

if "student_id" not in st.session_state:
    st.warning("Please login first.")
    st.stop()

subjects = get_subjects(st.session_state.student_id)

if not subjects:
    st.warning("Please add subjects first.")
    st.stop()

st.subheader("📅 Enter Exam Date")

exam_date = st.date_input(
    "Select Your Exam Date",
    min_value=datetime.date.today()
)

today = datetime.date.today()
days_left = (exam_date - today).days

st.write(f"📆 Days Remaining: {days_left} days")

# 🔥 Important: Only calculate when user clicks
if st.button("Check My Stress Level"):

    if days_left <= 3:
        urgency = "High"
    elif days_left <= 7:
        urgency = "Medium"
    else:
        urgency = "Low"

    stress = calculate_stress(
        len(subjects),
        st.session_state.study_hours,
        urgency
    )

    st.subheader("📊 Stress Level Result")
    st.success(stress)
