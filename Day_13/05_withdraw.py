balance = 1000

def withdraw(amount):
    global balance
    balance = balance - amount
    print(balance)


withdraw(200)
withdraw(300)

print(balance)