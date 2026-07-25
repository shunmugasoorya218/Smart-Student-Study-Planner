def generate_schedule(subjects, study_hours):
    schedule = []

    total_subjects = len(subjects)

    for subject, level in subjects:

        if level == "Hard":
            hours = study_hours * 0.5
        elif level == "Medium":
            hours = study_hours * 0.3
        else:
            hours = study_hours * 0.2

        schedule.append((subject, level, round(hours, 2)))

    return schedule