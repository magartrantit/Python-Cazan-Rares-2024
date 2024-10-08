import math

numbers = input("Dati un sir de numere separate prin spatiu: ").split()
numbers = list(map(int, numbers))

def gcd(a, b):
    return math.gcd(a, b)

result = numbers[0]

for i in numbers:
    result = gcd(result, i)\

print("Cmmdc este: ", result)