def say_hello():
    print("hello")


def decorator(func):

    def wrapper():
        print("Before")
        func()
        print("After")

    return wrapper

x = decorator(say_hello)
x()