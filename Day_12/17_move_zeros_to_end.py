numbers = [0, 10, 0, 20, 30, 0, 40]

non_zero = []
zeros = []

for number in numbers:
    if number == 0:
        zeros.append(number)
    else:
        non_zero.append(number)

non_zero.extend(zeros)

print("non zero =",non_zero)


