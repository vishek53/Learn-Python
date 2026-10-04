def calculator(a, b):
    total = a + b
    difference = a - b
    product = a * b
    division = a / b

    return total, difference, product, division

num1 = int(input("Enter your number 1: "))
num2 = int(input("Enter your number 2: "))

result1, result2, result3, result4 = calculator(num1, num2)

print("Sum =", result1)
print("Difference =", result2)
print("Product =", result3)
print("Division =", result4)