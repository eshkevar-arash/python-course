def func(x):
    return x + 1


li = [1, 2, 3]
# a = map(lambda x: x + 1, li)
# print(list(a))

# li_2 = [item * 2 for item in li]
# print(li_2)
# a = list(filter(lambda item: item % 2 == 0, li))
# print(a)
names = ["arash", "adel", "aref"]
res = [item.upper() for item in names]
print(res)