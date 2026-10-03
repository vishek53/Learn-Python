def student_result(name, marks):

    if marks >= 40:
        return "Pass"
    else:
        return "Fail"

result1 = student_result("Vishek", 89)
result2 = student_result("Sanskriti", 87)
result3 = student_result("aiswariya", 32)

print("Vishek =", result1)
print("Sanskriti =", result2)
print("aiswariya =", result3)