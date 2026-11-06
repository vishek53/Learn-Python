
students = []

# Collect information for 3 students
for i in range(3):
    print(f"\n========== STUDENT {i + 1} ==========")

    name = input("Enter student name: ")
    roll_number = input("Enter roll number: ")

    marks = []

    for j in range(3):
        subject_marks = float(input(f"Enter marks for Subject {j + 1}: "))
        marks.append(subject_marks)

    # Calculate total and average
    total = sum(marks)
    average = total / 3

    # Check pass or fail
    if marks[0] >= 33 and marks[1] >= 33 and marks[2] >= 33:
        status = "PASS"
    else:
        status = "FAIL"

    # Store student information
    student = {
        "name": name,
        "roll_number": roll_number,
        "marks": marks,
        "total": total,
        "average": average,
        "status": status
    }

    students.append(student)


# Display individual student reports
print("\n\n========== STUDENT REPORTS ==========")

for student in students:
    print("\n------------------------------------")
    print("         STUDENT REPORT")
    print("------------------------------------")

    print(f"Name: {student['name']}")
    print(f"Roll Number: {student['roll_number']}")

    for j in range(3):
        print(f"Subject {j + 1}: {student['marks'][j]}")

    print(f"Total Marks: {student['total']} / 300")
    print(f"Average: {student['average']:.2f}")
    print(f"Status: {student['status']}")


# Find the student with the highest average
top_student = students[0]

for student in students:
    if student["average"] > top_student["average"]:
        top_student = student


# Display top performer
print("\n\n------------------------------------")
print("           TOP PERFORMER")
print("------------------------------------")

print(f"Name: {top_student['name']}")
print(f"Roll Number: {top_student['roll_number']}")
print(f"Average: {top_student['average']:.2f}")
