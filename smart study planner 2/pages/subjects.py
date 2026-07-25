import streamlit as st
from database.db import add_subject, get_subjects

st.title("📚 Add Subjects")

if "student_id" not in st.session_state:
    st.warning("Please login first!")
else:
    subject = st.text_input("Subject Name")

    level = st.radio(
        "Select Difficulty",
        ["Easy", "Medium", "Hard"],
        horizontal=True
    )

    if st.button("Add Subject"):
        if subject:
            add_subject(st.session_state.student_id, subject, level)
            st.success("Subject Added ✅")

    st.subheader("Your Subjects")
    subjects = get_subjects(st.session_state.student_id)
    for sub in subjects:
        st.write(f"• {sub[0]} ({sub[1]})")
