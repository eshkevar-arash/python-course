def outer():
    def inner():
        return "inner-func is run"
    return inner

x = outer()
res = x()
print(res)