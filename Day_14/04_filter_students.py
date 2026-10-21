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

    average = total/ len(marks)

    return average

qualified_students = []
for student in students:
    name = student["name"]
    marks = student["marks"]

    average = calculate_average(marks)

    if average >= 80:
        qualified_students.append({
            "name": name,
            "average": average
            })

print("students with average >= 80")

for student in qualified_students:
    print(f"{student['name']}: {student['average']:.2f}")