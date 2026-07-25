import streamlit as st
import random

st.title("🎯 Number Guessing Game")

# 🔒 LOGIN CHECK (optional)
if "student_id" not in st.session_state:
    st.warning("⚠️ Please login first!")
    st.stop()

# ============================
# 🔹 INITIALIZE GAME
# ============================

if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)

if "attempts" not in st.session_state:
    st.session_state.attempts = 0

# ============================
# 🔹 USER INPUT
# ============================

guess = st.number_input("Enter your guess (1 - 100)", 1, 100)

if st.button("Submit Guess"):

    st.session_state.attempts += 1

    if guess < st.session_state.number:
        st.warning("📉 Too low! Try again")

    elif guess > st.session_state.number:
        st.warning("📈 Too high! Try again")

    else:
        st.success(f"🎉 Correct! You guessed in {st.session_state.attempts} attempts")

        if st.session_state.attempts <= 5:
            st.balloons()
            st.success("🔥 Excellent!")
        else:
            st.info("👍 Good job!")

        # Reset game
        st.session_state.number = random.randint(1, 100)
        st.session_state.attempts = 0

# ============================
# 🔄 RESET BUTTON
# ============================

if st.button("🔄 Restart Game"):
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.info("Game restarted!")