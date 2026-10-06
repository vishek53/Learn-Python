numbers = [10, 45, 23, 67, 12, 89, 34]

even = 0
odd = 0

for number in numbers:
    if number % 2 == 0:
        even = even + 1
    else:
         odd = odd + 1

print("Even =",even)
print("Odd =",odd)
