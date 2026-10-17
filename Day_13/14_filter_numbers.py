numbers = [12, 7, 25, 4, 18, 9, 30, 11, 6]


def filter_even(numbers):
    even_number = []

    for number in numbers:
        if number % 2 == 0:
            even_number.append(number)

    return even_number


def analyze_numbers(numbers):
    even = filter_even(numbers)
    count= len(even)

    print("Even numbers:", even)
    print("Count:",count)


analyze_numbers(numbers)
    