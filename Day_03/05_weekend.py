# 1 = Monday
# 2 = Tuesday
# 3 = Wednesday
# 4 = Thursday
# 5 = Friday
# 6 = Saturday
# 7 = Sunday

day = int(input("Enter the day no: "))

if day == 6 or day == 7:
    print("It's a weekend.")
else:
    print("It's a weekday.")