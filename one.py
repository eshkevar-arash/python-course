def func(a, b, *c, d):
    return d


x = func(1, 2, 3, 4, d=5)
print(x)
