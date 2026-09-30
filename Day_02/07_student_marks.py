name = input("enter student name: ")
marks1 = float(input("enter student marks1: "))
marks2 = float(input("enter student marks2: "))
marks3 = float(input("enter student marks3: "))

total = marks1 + marks2 + marks3
average = total / 3
print(f"student name: {name}")
print(f"total marks: {total}")
print(f"average marks: {average}")