numbers = [-5, 10, -2, 7, 0, 15, -8, 20]

even = 0
odd = 0
for number in numbers:
    if number % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print("Count even =",even)
print("Count odd =",odd)