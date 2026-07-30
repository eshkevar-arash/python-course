def my_sort(s):
    def descending(l):
        return sorted(l)

    def ascending(l):
        return sorted(l, reverse=True)
    if s == "a":
        return ascending
    elif s == "d":
        return descending

myList = [1,3,2,5,4,7,6]
print(myList)
action = input("enter action: ")
f = my_sort(action)
print(f(myList))