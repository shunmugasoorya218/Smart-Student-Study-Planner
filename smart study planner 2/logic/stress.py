def calculate_stress(num_subjects, study_hours, urgency):

    base_stress = num_subjects * 10

    if study_hours < 3:
        base_stress += 20
    elif study_hours < 5:
        base_stress += 10

    if urgency == "High":
        base_stress += 30
    elif urgency == "Medium":
        base_stress += 15

    if base_stress < 40:
        return "😊 Low Stress – You are doing great!"
    elif base_stress < 70:
        return "😐 Medium Stress – Stay consistent!"
    else:
        return "😰 High Stress – Focus and plan better!"