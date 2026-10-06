numbers = [10, 45, 23, 67, 12, 89, 34]

limit = int(input("Enter the limit:"))

greater_numbers = []

for num in numbers:
    if limit < num:
        greater_numbers.append(num)

print(greater_numbers)