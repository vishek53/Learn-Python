name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))
current_year = int(input("Enter your current year: "))

if current_year<birth_year:
    print("Error: Please enter valid years.")

else:
    age = current_year - birth_year

    print(f"hello {name}!")
    print(f"Your age is approximately {age} years.")