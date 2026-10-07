numbers = numbers = [10, -5, 20, -8, 30, -2, 40]

positive = []
negative = []

for number in numbers:
    if number < 0:
        negative.append(number)
    else:
        positive.append(number)

negative.extend(positive)

print("positive =",negative)