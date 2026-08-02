def my_sort(action):
    def descending(l):
        return sorted(l)

    def ascending(l):
        return sorted(l, reverse=True)

    def error(l):
        return f"Error!!!, {action}"


    if action == "a":
        return ascending
    elif action == "d":
        return descending
    else:
        return error


l = [2, 1, 4, 3, 6, 5]
print(l)
action = input("enter action: \n")
f = my_sort(action)
print(f(l))