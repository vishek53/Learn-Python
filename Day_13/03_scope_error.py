score = 50


def add_bonus():
    score = score + 10
    print(score)


add_bonus()
print(score)


# UnboundLocalError
# Because we're assigning to score inside the function, Python treats it as a local variable. But we're trying to use that local variable before giving it a value.