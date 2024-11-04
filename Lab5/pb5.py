def putere(x, n):
    if n == 0:
        return 1
    else:
        res = x
        for i in range(1, n):
            res = res * x
    return res%10

print (putere(2, 3))


# SAU

print(x%10**n)