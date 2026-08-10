def say_hello():
    print("Hello arash")


def say_bye():
    print("by arash")
def wrapper(f):
    print("Before")
    f()
    print("After")


wrapper(say_bye)