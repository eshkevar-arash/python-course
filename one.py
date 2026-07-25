def xxx(**m):
    return m["y"]


d = {
    "x": 1,
    "y": 2,
    "z": 3
}
x = xxx(**d)
print(x)
