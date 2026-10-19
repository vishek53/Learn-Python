numbers = [12, -7, 25, -4, 0, 18, -9, 30, -11, 0]

def filter_even(numbers):
    even_numbers =[]

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)

    return even_numbers


def filter_odd(numbers):
    odd_number = []

    for number in numbers:
        if number % 2 != 0:
            odd_number.append(number)

    return odd_number

def analyze_numbers(numbers):
    even = filter_even(numbers)
    odd = filter_odd(numbers)

    print(f"Even numbers: {even}")
    print(f"Even count:{len(even)}")
    print(f"Odd numbers: {odd}")
    print(f"Odd count: {len(odd)}")

analyze_numbers(numbers)