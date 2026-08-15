def dec(func):
    def inner():
        print("inner Run")
        func()
    return inner

def f():
    print("hello")


f = dec(f)
f()


