numbers = [10, 45, 23, 67, 12, 89, 34]

largest = numbers[0]
smallest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number

difference = largest - smallest 

print("largest: ",largest)
print("smallest: ",smallest)
print("difference: ",difference)
