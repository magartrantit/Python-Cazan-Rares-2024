def operatii(a, b):
    set_a = set(a)
    set_b = set(b)
    print("Union: ", set_a.union(set_b))
    print("Intersection: ", set_a.intersection(set_b))
    print("Difference: ", set_a.difference(set_b))
    print("Difference: ", set_b.difference(set_a))


a = input("Prima lista: ").split(",")
b = input("A doua lista: ").split(",")
operatii(a, b)