def sortare(txt):
    res = sorted(txt.split(" "), key = lambda x: (len(x), x))
    return res

print(sortare("ana are zere si pere"))