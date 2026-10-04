def student_result(name, marks):
    if marks >= 40:
        return "Pass"
    else:
        return "Fail"
 
 
result1 = student_result("Vishek", 89)
result2 = student_result("Sanskriti", 87)
result3 = student_result("Aiswariya", 32)
 
print(f"Vishek = {result1}")
print(f"Sanskriti = {result2}")
print(f"Aiswariya = {result3}")
 