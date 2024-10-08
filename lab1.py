import random

r = random.choice(range(100))

def dist(a, b):
    return abs(a - b)

while True:
    print("Dati un numar de la 1 la 100")
    user_input = int(input())
    if dist(r, user_input) == 0:
        print("Ai ghicit")
        break
    elif user_input > 100 or user_input < 1:
        print("numar invalid")
    elif dist(r, user_input) < 10:
        print("fierbinte")
    elif dist(r, user_input) < 50:
        print("calda")
    
    else:
        print("rece")