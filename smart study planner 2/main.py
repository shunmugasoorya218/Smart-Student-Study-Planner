import streamlit as st
from database.db import create_tables

st.set_page_config(page_title="Smart Study Planner", page_icon="📚", layout="wide")

create_tables()

# 🔥 HEADER
col1, col2 = st.columns([8,2])

with col1:
    st.title("🎓 Smart Study Planner")

with col2:
    if "student_name" in st.session_state:
        st.success("👤 " + st.session_state.student_name)

st.markdown("---")
st.markdown("### Plan Smart. Study Smart. Succeed Smart 🚀")

st.sidebar.success("Select a page 👆")
