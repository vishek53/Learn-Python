score = 50


def add_bonus():
    global score
    score = score + 10
    print(score)


add_bonus()
print(score)