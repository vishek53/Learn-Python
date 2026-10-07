numbers = [10, 20, 20, 30, 10, 40, 30, 20, 50, 10]

frequency = {}
seen = []
duplicates = []


# Count frequency and find duplicates
for number in numbers:

    # Count how many times each number appears
    if number in frequency:
        frequency[number] = frequency[number] + 1
    else:
        frequency[number] = 1

    # Find duplicate numbers
    if number in seen:
        if number not in duplicates:
            duplicates.append(number)
    else:
        seen.append(number)


# Print frequency of all numbers
print("Frequency:")

for key in frequency:
    print(key, "=", frequency[key])


# Find the most frequent number
most_frequent = None
highest_frequency = 0

for key in frequency:

    if frequency[key] > highest_frequency:
        highest_frequency = frequency[key]
        most_frequent = key


print("Most frequent:", most_frequent)
print("Frequency:", highest_frequency)
print("Duplicates:", duplicates)