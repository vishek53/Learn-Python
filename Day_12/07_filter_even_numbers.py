numbers = [10, 45, 23, 67, 12, 89, 34]

limit = int(input("Enter the limit:"))

greater_and_even_numbers = []

for num in numbers:
    if limit < num:
        if num % 2 ==0:
               greater_and_even_numbers.append(num)

print(greater_and_even_numbers)