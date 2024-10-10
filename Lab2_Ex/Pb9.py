def first_last_letter(s):
    cuv = ""
    for i in s:
        cuv = cuv + i
        if i == " ":
            print(cuv[0] + cuv[-2], end = " ")
            cuv = ""
    print(cuv[0] + cuv[-1])       
    

s = input("Dati sirul: ")
first_last_letter(s)