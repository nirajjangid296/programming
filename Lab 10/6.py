def get_grade(marks):
    if marks >= 80:
        return "A"
    if marks >= 60:
        return "B"
    if marks >= 40:
        return "C"
    return "F"


student_count = int(input())
grade_counts = {}

for i in range(student_count):
    name, marks = input().split()
    grade = get_grade(int(marks))
    print(f"{name}: {grade}")
    grade_counts[grade] = grade_counts.get(grade, 0) + 1
print("Grade count:")
print(grade_counts)
