x = 10
def A():
    x = 11

    def B():
        global x
        x += 1
        print(x)
    B()

A()
print(x)