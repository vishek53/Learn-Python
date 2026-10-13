def calculate_total(marks):
    return sum(marks)

def calculate_average(total, subjects):
    return total / subjects

def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "fail"

def display_report(name, total, average, grade):
    print("Student:", name)
    print("Total Marks:", total)
    print("Average:", average)
    print("Grade:", grade)

marks = [85, 92, 78, 95, 80]  
name = "Alex" 
total = calculate_total(marks)
average = calculate_average(total, len(marks))
grade = get_grade(average)

display_report(name, total, average, grade)