def dec(func):
    def inner():
        print("inner Run")
        func()
    return inner

@dec
def f():
    print("hello")
f()





