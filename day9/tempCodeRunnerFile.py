for item in student_scores:
    student_grades = student_scores
    if student_scores[item] >= 91:
        student_grades[item] = "outstanding"
    elif student_scores[item] >= 81 and student_scores[item] <= 90:
        student_grades[item] = "exceeds expectations"
    elif student_scores[item] >= 71 and student_scores[item] <= 80:
        student_grades[item] = "acceptable"
    else:
        student_grades[item] = "fail"