from functools import reduce

s = "12.012w"


def is_numeric(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
print(is_numeric(s))