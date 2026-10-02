python_club = {"vishek", "sanskriti", "yash", "pranjal"}
ai_club = {"vishek", "sanskriti", "priya", "arjun"}

students_in_both_clubs = python_club & ai_club
print(students_in_both_clubs)

students_only_in_python_club = python_club - ai_club
print(students_only_in_python_club)

students_in_either_club = python_club | ai_club
print(students_in_either_club)