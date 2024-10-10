def parantezare(expr):
    ct1 = 0
    ct2 = 0
    for i in expr:
        if i == "(":
            ct1 += 1
        if i == ")":
            ct2 += 1
        if(ct2 > ct1):
            return False
    if ct1 == ct2:
        return True
    return False
    
expr = input("Dati expresia: ")
if parantezare(expr):
    print("Expresia este corecta")
else:
    print("Expresia nu este corecta")