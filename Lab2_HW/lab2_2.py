s = input("Dati un string: ")

def vowels(s):
    ct = 0
    for i in s:
        if i in "aeiouAEIOU":
            ct = ct + 1
    return ct

print("Numarul de vocale este: ", vowels(s))
