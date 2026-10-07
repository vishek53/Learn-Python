numbers = [10, 20, 30, 40, 50]

rotated = []

rotated.append(numbers[-1])

for i in range(len(numbers) -1):
    rotated.append(numbers[i])

print(rotated)