numbers = [12, -7, 25, -4, 0, 18, -9, 30, -11, 0]

def find_largest(numbers):
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number
    return largest

def find_smallest(numbers):
    smallest = numbers[0]

    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

def analyze_numbers(numbers):
    largest = find_largest(numbers)
    smallest = find_smallest(numbers)

    print(f"Largest number: {largest}")
    print(f"Smallest number: {smallest}")
            
analyze_numbers(numbers)