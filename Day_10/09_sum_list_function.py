def sum_list(numbers):
    total = 0

    for number in numbers:
        total = total + number

    return total

numbers = [10, 20, 30, 40, 50]

result = sum_list(numbers)

print("sum =", result)