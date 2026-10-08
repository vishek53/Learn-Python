x = 10          # global x

def test():
    x = 20      # local x
    print(x)    # prints local x

test()
print(x)        # prints global x