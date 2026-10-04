numbers = [-5, 10, -2, 7, 0, 15, -8, 20]

positive = 0
negative = 0
zero = 0
even = 0
odd = 0
total = 0

#for positive count
for number in numbers:
    if number > 0:
        positive = positive + 1
print("Positive numbers=",positive)

#for negative count
for number in numbers:
    if number < 0:
        negative = negative + 1
print("negative numbers=",negative)

#for zero count
for number in numbers:
    if number == 0:
        zero = zero + 1
print("zero numbers=",zero)

#for even and odd count
for number in numbers:
    if number % 2 == 0:
        even = even + 1

    else:
        odd = odd +1
        
print("even numbers=",even)
print("odd numbers",odd)

#for total
for number in numbers:
    total = total + number
print("sum =",total)