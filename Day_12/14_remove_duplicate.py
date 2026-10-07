numbers = [10, 20, 20, 30, 10, 40, 30, 50]

unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print(unique_numbers)