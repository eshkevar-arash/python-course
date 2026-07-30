def descending(l):
    return sorted(l)


def ascending(l):
    return sorted(l, reverse=True)


def mySort(f, l):
    return f(l)

my_list = [1,4,2,6,3,8]
ascending_list = mySort(ascending, my_list)
print(ascending_list)

descending_list = mySort(descending, my_list)
print(descending_list)