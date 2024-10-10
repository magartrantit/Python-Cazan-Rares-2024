def convert(sir, nr):
    L = len(sir)
    result = 0
    mult = 1
    while nr > 0:
        result += (nr % L) * mult
        nr = nr // L
        mult *= 10
    return result

sir = input("Dati sirul de caractere: ")
nr = int(input("Dati numarul: "))
print(convert(sir, nr))