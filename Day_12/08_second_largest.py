numbers = [10, 45, 23, 67, 12, 89, 34]

largest = numbers[0]
second_largest = numbers[1]

for number in numbers:
    if number > largest:
        second_largest = largest
        largest = number
    elif number > second_largest:
        second_largest = number

print("second_largest =", second_largest)