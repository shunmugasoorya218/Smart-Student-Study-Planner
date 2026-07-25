import streamlit as st
from database.db import add_student, get_student

st.title("👤 Student Login")

name = st.text_input("Name")
age = st.number_input("Age", 10, 30)
grade = st.text_input("Class / Year")
study_hours = st.slider("Study Hours Per Day", 1, 10, 4)

if st.button("Login"):

    if name:

        student_data = get_student(name)

        if student_data:
            st.session_state.student_id = student_data[0]
            st.session_state.study_hours = student_data[4]
            st.session_state.student_name = name
            st.success(f"Welcome Back {name} 👋")

        else:
            student_id = add_student(name, age, grade, study_hours)
            st.session_state.student_id = student_id
            st.session_state.study_hours = study_hours
            st.session_state.student_name = name
            st.success("Profile Created Successfully ✅")

    else:
        st.warning("Enter your name!")
