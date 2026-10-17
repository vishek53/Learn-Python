numbers = [12, -7, 25, -4, 0, 18, -9, 30, -11]

def filter_positive(numbers):
    positive_number = []

    for number in numbers:
        if number > 0:
            positive_number.append(number)

    return positive_number

def filter_negative(numbers):
    negative_number = []

    for number in numbers:
        if number < 0:
            negative_number.append(number)

    return negative_number


def analyze_numbers(numbers):
    positive = filter_positive(numbers)
    p_count= len(positive)
    negative = filter_negative(numbers)
    n_count= len(negative)

    print("Positive numbers:", positive)
    print("posititve Count:",p_count)
    print("Negative numbers:", negative)
    print("Negative Count:",n_count)


analyze_numbers(numbers)
    