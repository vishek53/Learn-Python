def count_passed(marks):
    passed = 0
    
    for mark in marks:
            if mark >=40:
                passed = passed + 1

    return passed

def count_failed(marks):
    failed = 0
    for mark in marks:
        if mark <=40:
            failed = failed + 1

    return failed


def analayze_performance(marks):
    passed = count_passed(marks)
    failed = count_failed(marks)

    print("passed subject:",passed)
    print("failed subject:",failed)

marks = [45, 82, 33, 91, 67, 28, 75]

analayze_performance(marks)