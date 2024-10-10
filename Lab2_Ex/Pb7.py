def majuscule(s):
    ct = 0
    for i in s:
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            ct += 1
    return ct

s = input("Dati sirul: ")
print(majuscule(s))