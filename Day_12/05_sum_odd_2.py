# 2nd way of doin sum of odd numbers

numbers = [10, 45, 23, 67, 12, 89, 34]

odd_numbers = []

for num in numbers:
    # if num % 2 == 1:
    if num % 2 != 0:
        odd_numbers.append(num)
    
total = 0

for num in odd_numbers:
    total = total + num

print(odd_numbers)
print("Sum =",total)