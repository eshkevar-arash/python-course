
def func_isChar(ch):
    ascii_cod = ord(ch)
    if (97 <= ascii_cod <= 122) | (48 <= ascii_cod <= 57) | (65 <= ascii_cod <= 90):
        return True

    return False


ch = input("enter a charactor: \n")[0]
print(ch)
isChar = func_isChar(ch)
print(isChar)

