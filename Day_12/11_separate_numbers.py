numbers = [10, -5, 0, 23, -8, 0, 15, -2]

positive = []
negative = []
zero = []

for number in numbers:
    if number > 0:
         positive.append(number)
    elif number < 0:
        negative.append(number)
    else:
        zero.append(number)

print("positive =", positive)
print("negative =", negative)
print("zero = ", zero)