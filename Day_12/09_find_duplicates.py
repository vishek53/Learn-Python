numbers = [10, 20, 30, 20, 40, 10, 50]

seen = []
duplicates = []

for number in numbers:
    if number in seen:
        duplicates.append(number)
    else:
        seen.append(number)

print(duplicates)