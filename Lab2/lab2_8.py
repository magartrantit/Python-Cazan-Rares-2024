text = input("Dati un text: ")

ct = 0
for i in text:
    if i in " ":
        ct = ct + 1

ct = ct + 1
print("Numarul de cuvinte din text este: ", ct)