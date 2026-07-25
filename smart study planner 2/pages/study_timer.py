import streamlit as st
import time

st.title("⏱️ Study Timer")

# 🔒 LOGIN CHECK (optional, remove if not needed)
if "student_id" not in st.session_state:
    st.warning("⚠️ Please login first!")
    st.stop()

# ============================
# 🔹 INITIALIZE STATE
# ============================

if "timer_running" not in st.session_state:
    st.session_state.timer_running = False

if "time_left" not in st.session_state:
    st.session_state.time_left = 0

# ============================
# 🔹 INPUT TIME
# ============================

minutes = st.slider("Set Study Time (minutes)", 1, 60, 25)

# ============================
# 🔹 BUTTONS
# ============================

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("▶ Start"):
        if not st.session_state.timer_running:
            st.session_state.time_left = minutes * 60
            st.session_state.timer_running = True

with col2:
    if st.button("⏸ Stop"):
        st.session_state.timer_running = False

with col3:
    if st.button("🔄 Reset"):
        st.session_state.timer_running = False
        st.session_state.time_left = 0

# ============================
# 🔹 TIMER DISPLAY
# ============================

timer_placeholder = st.empty()

# ============================
# 🔹 RUN TIMER
# ============================

if st.session_state.timer_running:

    while st.session_state.time_left > 0 and st.session_state.timer_running:
        mins, secs = divmod(st.session_state.time_left, 60)
        timer_placeholder.markdown(f"## ⏳ {mins:02d}:{secs:02d}")
        time.sleep(1)
        st.session_state.time_left -= 1

    # When finished
    if st.session_state.time_left == 0:
        st.session_state.timer_running = False
        timer_placeholder.markdown("## ⏰ 00:00")
        st.success("✅ Time's up! Take a break 🎉")

else:
    mins, secs = divmod(st.session_state.time_left, 60)
    timer_placeholder.markdown(f"## ⏳ {mins:02d}:{secs:02d}")