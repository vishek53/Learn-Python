numbers = [10, 45, 23, 67, 12, 89, 34]

smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number

print("smallest =",smallest)
