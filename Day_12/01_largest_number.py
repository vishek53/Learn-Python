numbers = [10, 45, 23, 67, 12, 89, 34]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("largest =",largest)
