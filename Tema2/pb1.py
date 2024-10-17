n = int(input("Enter a number: "))
def fibo(n):
    list = []
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        list = [0]
        return list
    elif n == 2:
        list = [0,1]
        return list
    else:
        a = 0
        b = 1
        list = [a, b]
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            list += [c]
    return list
        
print(fibo(n))