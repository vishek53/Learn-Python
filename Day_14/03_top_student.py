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

highest_average = 0
top_student = ""

for student in students:
    name = student["name"]
    marks = student["marks"]

    average = calculate_average(marks)

    if average > highest_average:
        highest_average = average
        top_student = name


print("Top student:",top_student)
print("Average marks:", round(highest_average, 2))
