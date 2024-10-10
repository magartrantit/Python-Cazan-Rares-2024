def cons_voc(s):
    ctc = 0
    ctv = 0
    for i in s:
        if i in "aeiou":
            ctv += 1
        if i in "bcdfghjklmnpqrstvwxyz":
            ctc += 1
    print("Consoane: ", ctc)
    print("Vocale: ", ctv)

s = input("Dati sirul: ")
cons_voc(s)