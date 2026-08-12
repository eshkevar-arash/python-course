# def say_hello(name):
#     print(f"Hello {name}")
#
#
# def say_by():
#     print("by")
#
#
# def decorator(func):
#     def wrapper(name):
#         print("before")
#         func(name)
#         print("after")
#
#     return wrapper
#
#
# # say_hello = decorator(say_hello)
# say_hello("arash")

# say_by = decorator(say_by)
# say_by()


def func(*args):
    print(type(args))
    return args


x = func(10, 20, 30, 40)
print(x)
