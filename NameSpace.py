l = [100, 20, 3, 80, 600]


def func_max(iterable):
    mx = iterable[0]
    for i in range(len(iterable) - 1):
        if iterable[i + 1] > mx:
            mx = iterable[i + 1]

    return mx


mx = func_max(l)
print(mx)
