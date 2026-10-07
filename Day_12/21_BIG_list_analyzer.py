numbers = [10, -5, 23, 0, 67, -8, 12, 89, -2, 34]

largest = numbers[0]
smallest = numbers[0]

total = 0

positive = 0
negative = 0
zero = 0

even = 0
odd = 0

for number in numbers:
    if number > largest:
        largest = number

    if number < smallest:
        smallest = number

    total = total + number

    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1
    else:
        zero += 1

    if number % 2 == 0:
        even += 1
    else:
        odd += 1

print("largest =", largest)
print("smallest =", smallest)
print("total =", total)
print("positive =", positive)
print("negative =", negative)
print("zero =", zero)
print("even =", even)
print("odd =", odd)