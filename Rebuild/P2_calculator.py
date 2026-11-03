a = float(input("Enter first number:"))
b = float(input("Enter second number:"))

addition = a + b
subtraction = a - b
multiplication = a * b
if b!= 0:
    division = a / b
    floor_division = a // b
    modulus = a % b

    print(f"Division: {division}")
    print(f"Floor Division: {floor_division}")
    print(f"Modulus: {modulus}")
else:
    print("Error: Division by zero is not defined.")


print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")


