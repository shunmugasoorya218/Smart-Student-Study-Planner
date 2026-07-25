import streamlit as st

st.title("📊 Dashboard")

if "student_id" not in st.session_state:
    st.warning("Please login first!")
else:
    st.success("Welcome to your Smart Dashboard 🚀")
    st.markdown("### Choose options from sidebar:")
    st.markdown("- Add Subjects")
    st.markdown("- Generate Schedule")
    st.markdown("- Check Exams")
