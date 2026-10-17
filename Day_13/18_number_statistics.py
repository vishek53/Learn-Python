
numbers = [12, -7, 25, -4, 0, 18, -9, 30, -11, 0]


def calculate_sum(numbers):
    total = 0

    for number in numbers:
        total = total + number

    return total


def count_positives(numbers):
    count = 0

    for number in numbers:
        if number > 0:
            count = count + 1

    return count


def analyze_numbers(numbers):
    total = calculate_sum(numbers)
    positive_count = count_positives(numbers)

    print(f"Sum: {total}")
    print(f"Positive count: {positive_count}")


analyze_numbers(numbers)
