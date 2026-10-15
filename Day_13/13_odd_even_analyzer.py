
numbers = [12, 7, 25, 4, 18, 9, 30, 11, 6]


def count_even(numbers):
    even_count = 0

    for number in numbers:
        if number % 2 == 0:
            even_count += 1

    return even_count


def count_odd(numbers):
    odd_count = 0

    for number in numbers:
        if number % 2 != 0:
            odd_count += 1

    return odd_count


def analyze_numbers(numbers):
    even = count_even(numbers)
    odd = count_odd(numbers)

    print("Even numbers:", even)
    print("Odd numbers:", odd)


analyze_numbers(numbers)
