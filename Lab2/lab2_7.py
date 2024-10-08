nr = input("Dati un numar: ")

nr_bin = bin(int(nr))

ct = 0
for i in nr_bin:
    if i in "1":
        ct = ct + 1

print("Numarul de biti de 1 din reprezentarea binara a numarului dat este: ", ct)