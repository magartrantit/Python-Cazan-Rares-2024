def convert(nr):
    if nr == 0:
        return "0b0"
    bin = 0
    while nr > 0:
        bin = bin * 10 + nr % 2
        nr = nr // 2
    bin = str(bin)
    bin = bin[::-1]
    return "0b" + bin
print(convert(13))