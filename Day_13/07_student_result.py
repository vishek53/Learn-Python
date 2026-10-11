def calculate_total(marks):
    total = 0

    for mark in marks:
        total = total + mark

    return total

def calculate_average(total,number_of_subjects):
    return total / number_of_subjects

def get_result(average):
    if average >= 40:
        return "Pass"
    else:
        return "Fail"

marks = [80, 90, 70]

total = calculate_total(marks)
average = calculate_average(total, len(marks))
result = get_result(average)

print("Total:", total)
print("Average:", average)
print("Result:", result)