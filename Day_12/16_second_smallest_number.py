numbers = [10, 45, 23, 67, 12, 89, 34]

smallest = numbers[0]
second_smallest = numbers[1]

for number in numbers:
    if number < smallest:
        second_smallest = smallest
        smallest = number

    elif number < second_smallest and number != smallest:
        second_smallest = number

print("second_smallest =", second_smallest)
