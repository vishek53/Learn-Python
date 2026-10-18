numbers = [12, -7, 25, -4, 0, 18, -9, 30, -11, 0]

def calculate_sum(numbers):
    total = 0

    for number in numbers:
        total = total + number

    return total

def count_positives(numbers):
    p_count = 0

    for number in numbers:
        if number > 0 :
            p_count = p_count + 1

    return p_count


def count_negatives(numbers):
    n_count = 0

    for number in numbers:
        if number < 0 :
            n_count = n_count + 1

    return n_count

def count_zeros(numbers):
    z_count = 0 

    for number in numbers:
        if number == 0 :
            z_count = z_count + 1

    return z_count

def analyze_numbers(numbers):
        total = calculate_sum(numbers)
        positive_count = count_positives(numbers)
        negative_count = count_negatives(numbers)
        zeros_count = count_zeros(numbers)

        
        print(f"Sum: {total}")
        print(f"Positive count: {positive_count}")
        print(f"Negative count: {negative_count}")
        print(f"Zero count: {zeros_count}")


analyze_numbers(numbers)