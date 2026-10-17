numbers = [12, -7, 25, -4, 0, 18, -9, 30, -11, 0]

def count_zeros(numbers):
    zero = 0
    for number in numbers:
        if number == 0:
            zero = zero + 1

    return zero

def analyze_numbers(numbers):
    Zero_count = count_zeros(numbers)
    print(f"Zero Count: {Zero_count} ")
analyze_numbers(numbers)