def calculate_bonus(salary, performance):
    if performance == "excellent":
        return salary * 20 / 100
    elif performance == "good":
        return salary * 10 / 100
    elif performance == "average":
        return salary * 5 / 100
    else:
        return 0

def calculate_total_salary(salary, bonus):
    return salary + bonus

def get_salary_level(total_salary):
    if total_salary < 25000:
        return "Entry level"
    elif total_salary <= 50000:
        return "Mid level"
    else:
        return "Senior level"

salary = int(input("Enter employee salary: "))
performance = input("Enter employee performance: ").strip().lower()

bonus = calculate_bonus(salary, performance)
total_salary = calculate_total_salary(salary, bonus)
salary_level = get_salary_level(total_salary)

print("Bonus =", bonus)
print("Total Salary =", total_salary)
print("Salary Level =", salary_level)