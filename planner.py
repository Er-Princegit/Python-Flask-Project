def generate_plan(subject, hours, days, difficulty, goal):
    plan = []

    # 🎯 Difficulty impact
    if difficulty == "hard":
        extra = 2
    elif difficulty == "medium":
        extra = 1
    else:
        extra = 0

    # 🎯 Goal impact
    if goal == "exam":
        focus = "Revise + Practice"
        intensity = 1
    else:
        focus = "Learn + Practice"
        intensity = 0

    for day in range(1, days + 1):

        # 🔥 Smart pattern
        if day % 3 == 0:
            task = "Revision"
        elif day % 2 == 0:
            task = "Practice"
        else:
            task = "Learning"

        # 🔥 Adjust hours
        study_hours = hours + extra + intensity

        # 📅 Plan line
        plan.append(
            f"Day {day}: {task} {subject} ({focus}) for {study_hours} hours"
        )

    return plan