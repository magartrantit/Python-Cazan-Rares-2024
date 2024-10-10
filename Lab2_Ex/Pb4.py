def dec_to_hex(nr):
    if nr == 0:
        return "0x0"
    hex = ""
    while nr > 0:
        rest = nr % 16
        if rest < 10:
            hex = hex + str(rest)
        else:
            hex = hex + chr(55 + rest)
        nr = nr // 16
    hex = hex[::-1]
    return "0x" + hex

print(dec_to_hex(11))