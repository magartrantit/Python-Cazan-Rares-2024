def dup_unq(l):
    a = set()
    b = set()

    for i in l:
        if i in a:
            b.add(i)
            a.discard(i)
        else:
            a.add(i)
    return (len(a), len(b))

l = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8]
print(dup_unq(l))