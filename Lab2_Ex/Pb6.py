def convert(s):
    return hex(ord(s))[2:]

def ascii_to_hex(s):
    res = ""
    for i in s:
        if i == " ":
            res += "\n"
        else:
            res+= convert(i)
    print(res)

s = input("Dati sirul de caractere: ")
ascii_to_hex(s)