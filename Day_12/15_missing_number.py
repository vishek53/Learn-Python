numbers = [1, 2, 3, 4, 5, 7, 8, 9, 10]

actual_total = 0
expected_total = 0

for number in range(1, 11):
    expected_total = expected_total + number

for number in numbers:
    actual_total = actual_total + number

print("missing number =", expected_total - actual_total)