students = [
    {"name":"Aman", "marks": 85},
    {"name":"Riya", "marks": 92},
    {"name":"Raj", "marks": 74},
    {"name":"Neha", "marks": 88},
]
def display_students(students):
    for student in students:
        print(f'{student["name"]}: {student["marks"]}')

display_students(students)