numbers = [10, 20, 20, 30, 20, 40, 10, 50]

frequency = {}

for number in numbers:
    if number in frequency:
        frequency[number] = frequency[number] + 1
    else:
        frequency[number] = 1
        
for key in frequency:
    print(key, "=",frequency[key])