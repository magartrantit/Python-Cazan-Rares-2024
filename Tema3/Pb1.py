def operations(a, b):
    seta = set(a)
    setb = set(b)

    intersection = seta.intersection(setb)
    union = seta.union(setb)
    difference = seta.difference(setb)
    difference2 = setb.difference(seta)

    return [intersection, union, difference, difference2]


a = [1, 2, 3]
b = [3, 4, 5]
print(operations(a, b))