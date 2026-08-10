from itertools import count

counter = count(20)

while True:
    number = next(counter)
    print(number)
    if number == 30:
        break

