username = input("Enter your username: ").strip().lower()

if "@" in username :
    print("Valid username")
else: 
    print("Invalid username")