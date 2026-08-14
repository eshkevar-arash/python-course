def decorator(func):
    def wrapper(*args, **kwargs):
        print("before")

        result = func(*args, **kwargs)

        print("after")

        return result

    return wrapper





@decorator
def add(a, b):
    return a + b
res = add(2, 3)
print(res)