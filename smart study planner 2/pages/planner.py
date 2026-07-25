import streamlit as st
from database.db import get_subjects

st.title("📆 Smart Weekly Planner")

if "student_id" not in st.session_state:
    st.warning("Please login first!")
    st.stop()

subjects = get_subjects(st.session_state.student_id)

if not subjects:
    st.warning("Add subjects first!")
    st.stop()

subject_names = [sub[0] for sub in subjects]

days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

# 🔹 Time slots
weekday_slots = [
    "6:00 AM - 7:00 AM",
    "7:00 AM - 8:00 AM",
    "8:00 AM - 9:00 AM (Breakfast Break)",
    "10:00 AM - 12:00 PM",
    "12:00 PM - 1:00 PM (Lunch Break)",
    "4:00 PM - 6:00 PM",
    "8:00 PM - 9:00 PM"
]

weekend_slots = [
    "7:00 AM - 9:00 AM",
    "9:00 AM - 10:00 AM (Water Break)",
    "10:00 AM - 12:00 PM",
    "1:00 PM - 2:00 PM (Lunch Break)",
    "5:00 PM - 7:00 PM"
]

# 🔥 Store checklist state
if "completed_tasks" not in st.session_state:
    st.session_state.completed_tasks = {}

# ================================
# 🔄 DAY-WISE LOOP
# ================================
for day in days:

    st.markdown(f"# 📅 {day}")

    # Select slots
    if day in ["Saturday", "Sunday"]:
        slots = weekend_slots
    else:
        slots = weekday_slots

    # ============================
    # 📚 SCHEDULE
    # ============================
    st.subheader("📚 Schedule")

    day_tasks = []

    for i, slot in enumerate(slots):

        if "Break" in slot:
            st.write(f"⏸ {slot}")
        else:
            subject = subject_names[i % len(subject_names)]
            st.write(f"{slot} → 📖 {subject}")

            # store task
            day_tasks.append((slot, subject))

    # ============================
    # ✅ CHECKLIST
    # ============================
    st.subheader("✅ Checklist")

    completed_count = 0
    not_completed_count = 0

    for slot, subject in day_tasks:
        key = f"{day}_{slot}_{subject}"

        checked = st.checkbox(f"{slot} → {subject}", key=key)

        if checked:
            st.success(f"✔ {subject} completed")
            completed_count += 1
        else:
            st.error(f"❌ {subject} not completed")
            not_completed_count += 1

    # ============================
    # 📊 RESULT
    # ============================
    st.subheader("📊 Result")

    total = completed_count + not_completed_count

    if total > 0:
        progress = completed_count / total
        st.progress(progress)

        st.write(f"✅ Completed: {completed_count}")
        st.write(f"❌ Not Completed: {not_completed_count}")

        # 🔥 Message logic
        if not_completed_count > 0:
            st.warning("⚠️ Try to complete all the tasks!")
        else:
            st.success("🎉 Well done! Keep completing all tasks regularly!")

    st.markdown("---")