price = float(input("enter the priceof the item:"))
quantity=int(input("enter the quantity of the item:"))

total = price * quantity
total = round(total, 2)
print(f"Total bill amount: {total}")