
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

reversed_numbers = []

for i in range(len(numbers)-1,-1,-1):
    reversed_numbers.append(numbers[i])

print(reversed_numbers)