def calculate_discount(price, discount_percent):
    return price * discount_percent / 100


def calculate_final_price(price, discount):
    return price - discount


def get_price_category(final_price):
    if final_price < 500:
        return "budget"
    elif 500 <= final_price <= 1500:
        return "Mid-range"
    else:
        return "Premium"


price = float(input("Enter Price: "))
discount_percent = float(input("Enter discount percent: "))

discount = calculate_discount(price, discount_percent)
final_price = calculate_final_price(price, discount)
price_category = get_price_category(final_price)

print(f"Discount amount: {discount}")
print(f"Final price: {final_price}")
print(f"Category: {price_category}")