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


for student in students:
    average = calculate_average(student["marks"])
    print(f"{student['name']}: {average:}")
