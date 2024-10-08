str = input("Dati un text: ")

nr = ""

def extract_first_number(str):
    global nr
    for i in str:
        if i in "0123456789":
            nr = nr + i
        if nr != "" and i not in "0123456789":
            break
    return nr

extract_first_number(str)

if nr == "":
    print("Nu s-a gasit niciun numar in text")
else:
    print("Numarul gasit este: ", nr)
            