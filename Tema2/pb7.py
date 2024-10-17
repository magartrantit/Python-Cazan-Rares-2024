def palindrom(n):
    if n == int(str(n)[::-1]):
        return True
    return False

def tuplu(list):
    ctpal = 0
    maxpal = 0
    for i in list:
        if palindrom(i):
            ctpal += 1
            if i > maxpal:
                maxpal = i
    return (ctpal, maxpal)

list = [121, 123, 232, 12321, 123321, 12345, 123456, 1234567]
print(tuplu(list))