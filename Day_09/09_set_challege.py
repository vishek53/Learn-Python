python_club = {"vishek", "sanskriti","yash","pranjal"}
ai_club = {"vishek","sanskriti", "priya","arjun" }

student_in_both_club = python_club.intersection(ai_club)

print(student_in_both_club)

student_0nly_in_python_club = python_club.difference(ai_club)

print(student_0nly_in_python_club)

Students_in_either_club =  python_club.union(ai_club)

print(Students_in_either_club)
