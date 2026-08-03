x = 10
def A():
    x = 11
    print(x)

    def B():
        print(x)
    B()

