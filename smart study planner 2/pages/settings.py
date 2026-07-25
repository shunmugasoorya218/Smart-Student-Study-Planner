import streamlit as st
from database.db import connect

st.title("⚙️ Account Settings")

if "student_id" not in st.session_state:
    st.warning("Please login first.")
    st.stop()

conn = connect()
c = conn.cursor()

# 🔹 Edit Study Hours
st.subheader("⏳ Update Study Hours")

new_hours = st.slider("Change Daily Study Hours", 1, 12, st.session_state.study_hours)

if st.button("Update Study Hours"):
    c.execute("UPDATE students SET study_hours=? WHERE id=?",
              (new_hours, st.session_state.student_id))
    conn.commit()
    st.session_state.study_hours = new_hours
    st.success("Study hours updated successfully!")

# 🔹 Clear All Subjects
st.subheader("🗑 Reset Subjects")

if st.button("Delete All My Subjects"):
    c.execute("DELETE FROM subjects WHERE student_id=?",
              (st.session_state.student_id,))
    conn.commit()
    st.success("All subjects deleted!")

# 🔹 Logout
st.subheader("🚪 Logout")

if st.button("Logout"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.success("Logged out successfully!")
    st.rerun()

conn.close()
