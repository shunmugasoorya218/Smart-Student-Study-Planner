import streamlit as st
from database.db import get_subjects

st.title("🧠 Revision Booster")

# 🔒 LOGIN CHECK
if "student_id" not in st.session_state:
    st.warning("⚠️ Please login first!")
    st.stop()

# 🔹 Get subjects from DB
subjects_data = get_subjects(st.session_state.student_id)
subjects = [s[0] for s in subjects_data]

# ❌ If no subjects
if not subjects:
    st.warning("⚠️ Please add subjects first!")
    st.stop()

# ============================
# 🧠 REVISION BOOSTER
# ============================

selected = st.selectbox("📘 Choose Subject", subjects)

if st.button("🚀 Start Revision"):

    st.session_state.rev_questions = [
        f"Define {selected}",
        f"Explain key concepts of {selected}",
        f"List 5 important points in {selected}",
        f"What are applications of {selected}?",
        f"Write short notes on {selected}"
    ]

    st.session_state.rev_index = 0

# 🔹 Show questions
if "rev_questions" in st.session_state:

    current_q = st.session_state.rev_questions[st.session_state.rev_index]

    st.subheader(f"❓ Question {st.session_state.rev_index + 1}")
    st.write(current_q)

    if st.button("➡ Next"):
        st.session_state.rev_index += 1

        if st.session_state.rev_index >= len(st.session_state.rev_questions):
            st.success("🎉 Revision Completed!")
            del st.session_state.rev_questions
            del st.session_state.rev_index