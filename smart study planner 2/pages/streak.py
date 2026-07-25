import streamlit as st
from datetime import date, timedelta

st.title("🔥 Study Streak Tracker")

# 🔒 LOGIN CHECK
if "student_id" not in st.session_state:
    st.warning("⚠️ Please login first!")
    st.stop()

# ============================
# 🔹 INITIALIZE STATE
# ============================

if "streak" not in st.session_state:
    st.session_state.streak = 0

if "longest_streak" not in st.session_state:
    st.session_state.longest_streak = 0

if "last_study_date" not in st.session_state:
    st.session_state.last_study_date = None

today = date.today()

# ============================
# 🔥 MARK STUDY DONE
# ============================

if st.button("✅ Mark Today as Studied"):

    last_date = st.session_state.last_study_date

    if last_date is None:
        # First time
        st.session_state.streak = 1

    else:
        diff = (today - last_date).days

        if diff == 0:
            st.info("📅 Already marked today!")

        elif diff == 1:
            st.session_state.streak += 1

        else:
            st.session_state.streak = 1  # Reset streak

    # Update last study date
    st.session_state.last_study_date = today

    # Update longest streak
    if st.session_state.streak > st.session_state.longest_streak:
        st.session_state.longest_streak = st.session_state.streak

# ============================
# 📊 DISPLAY
# ============================

st.subheader("🔥 Current Streak")
st.success(f"{st.session_state.streak} days")

st.subheader("🏆 Longest Streak")
st.info(f"{st.session_state.longest_streak} days")

# ============================
# 🎯 MOTIVATION
# ============================

if st.session_state.streak == 0:
    st.warning("Start your streak today 🚀")

elif st.session_state.streak < 3:
    st.info("Good start! Keep going 👍")

elif st.session_state.streak < 7:
    st.success("🔥 You're building a habit!")

else:
    st.balloons()
    st.success("🏆 Amazing consistency!")