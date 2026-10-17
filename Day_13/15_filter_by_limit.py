numbers = [12, 7, 25, 4, 18, 9, 30, 11, 6]

def filter_greater(numbers, limit):
    greater_than_limit =[]

    for number in numbers:
        if number > limit:
            greater_than_limit.append(number)

    return greater_than_limit


def analyze_numbers(numbers, limit):
    filtered_numbers = filter_greater(numbers, limit)
    count = len(filtered_numbers)

    print(f"Numbers greater than{limit}: {filtered_numbers}")
    print(f"Count: {count}")

analyze_numbers(numbers, 25)