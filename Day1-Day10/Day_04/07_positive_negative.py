n = int(input("How many numbers: "))

positive = 0
negative = 0
zero = 0

for i in range(n):
    number = int(input("Enter number: "))

    if number > 0:
        positive = positive + 1

    elif number < 0:
        negative = negative + 1

    else:
        zero = zero + 1

print("Positive =", positive)
print("Negative =", negative)
print("Zero =", zero)