x = 30


def my_function():
    global x
    print(x)
    x = 45
    print(x)


my_function()