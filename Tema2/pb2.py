import math

list = input("Dati o lista seprata prin virgula: ").split(",")

def is_prime(n):
    if n < 2:
        return False
    for i in range (2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def lista_prime(list):
    ret_list = []
    for i in list:
        if is_prime(int(i)):
            ret_list += [int(i)]
    return ret_list

print(lista_prime(list))