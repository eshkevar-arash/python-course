def func(**a):
    return a["b"]


x = func(a=2, b=3)
print(x)
