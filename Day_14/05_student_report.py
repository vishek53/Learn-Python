
students = [
    {"name": "Aman", "marks": [80, 85, 90]},
    {"name": "Riya", "marks": [88, 92, 95]},
    {"name": "Raj", "marks": [70, 75, 80]},
    {"name": "Neha", "marks": [90, 85, 95]}
]


def calculate_average(marks):
    total = 0

    for mark in marks:
        total = total + mark

    average = total / len(marks)
    return average


passed_count = 0
failed_count = 0

highest_average = 0
top_student = ""


print("--- STUDENT PERFORMANCE REPORT ---")
print()

for student in students:
    name = student["name"]
    marks = student["marks"]

    average = calculate_average(marks)

    if average >= 80:
        status = "PASS"
        passed_count = passed_count + 1
    else:
        status = "FAIL"
        failed_count = failed_count + 1

    if average > highest_average:
        highest_average = average
        top_student = name

    print(f"{name:<4} | Average: {average:.2f} | Status: {status}")


print()
print("--- CLASS SUMMARY ---")
print(f"Total students: {len(students)}")
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")
print(f"Top student: {top_student}")
print(f"Top average: {highest_average:.2f}")
