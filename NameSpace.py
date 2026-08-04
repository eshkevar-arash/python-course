import copy
x = 1

l = [1,2,3]
s = 'arash'
t = (1, 2, 3)
sett = {1, 2, 3}


def func(a):
    a += [4, 6]
    print(a)

l_copy = copy.deepcopy(l)
func(l_copy)
print(l)
