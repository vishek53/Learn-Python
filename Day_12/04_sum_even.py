numbers = [10, 45, 23, 67, 12, 89, 34]

total = 0
even = 0

for num in numbers:
    if num % 2 == 0:
        even = even + 1
        total = total + num

print(total)