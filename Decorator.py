def outer():
    def inner():
        print("Hello")

    return inner


f = outer()
f()