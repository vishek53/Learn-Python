numbers = [2, 5, 3, 2, 8, 5, 9, 3, 2]

def find_duplicates(numbers):
    seen = []
    duplicates = []

    for number in numbers:
        if number in seen:
            if number not in duplicates:
                duplicates.append(number)
        else:
            seen.append(number)

    return duplicates

def analyze_numbers(numbers):
    duplicates = find_duplicates(numbers)

    print("Duplicates:", duplicates)
    print("Duplicate count:", len(duplicates))


analyze_numbers(numbers)