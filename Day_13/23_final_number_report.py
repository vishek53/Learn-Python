
numbers = [12, -7, 25, -4, 0, 18, -9, 30, -11, 0, 12]


def calculate_sum(numbers):
    total = 0

    for number in numbers:
        total = total + number

    return total


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


def count_positives(numbers):
    count = 0

    for number in numbers:
        if number > 0:
            count = count + 1

    return count


def count_negatives(numbers):
    count = 0

    for number in numbers:
        if number < 0:
            count = count + 1

    return count


def count_zeros(numbers):
    count = 0

    for number in numbers:
        if number == 0:
            count = count + 1

    return count


def analyze_numbers(numbers):
    print("Sum:", calculate_sum(numbers))
    print("Largest number:", find_largest(numbers))
    print("Smallest number:", find_smallest(numbers))
    print("Positive count:", count_positives(numbers))
    print("Negative count:", count_negatives(numbers))
    print("Zero count:", count_zeros(numbers))


analyze_numbers(numbers)
