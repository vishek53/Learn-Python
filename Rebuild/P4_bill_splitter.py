bill_amount = float(input("Enter the bil amount: "))
number_of_people = int(input("Enter the number of people: "))
tip_percentage = float(input("Enter the tip percentage: "))

if number_of_people <= 0:
    print("Error: Number of people must be greater than zero.")

elif bill_amount < 0:
    print ("Error: Bill amount cannot be negative.")

elif tip_percentage < 0:
    print("error: Tip percentage cannot be negative.")

else:
    tip_amount = bill_amount * tip_percentage / 100

    final_bill = bill_amount + tip_amount

    per_person = final_bill / number_of_people

    print(f"\nOriginal Bill:\t₹{bill_amount}")
    print(f"Tip Amount:\t₹{tip_amount}")
    print(f"Final Bill:\t₹{final_bill:.2f}")
    print(f"Amount Per Person:\t₹{per_person:.2f}")