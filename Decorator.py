def say_hello(name):
    print(f"hello {name}")


def add(a, b):
    return a + b


def decorator(func):
    def wrapper(*arg, **kwargs):
        print("before")
        result = func(*arg, **kwargs)
        print(result)
        print("after")
        return result

    return wrapper


add = decorator(add)

res = add(10, 20)
print(res)




