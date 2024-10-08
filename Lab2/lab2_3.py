s1 = input("Dati primul string: ")
s2 = input("Dati al doilea string: ")

def occurences(s1, s2):
    return s2.count(s1)

print("Numarul de aparitii este: ", occurences(s1, s2))
