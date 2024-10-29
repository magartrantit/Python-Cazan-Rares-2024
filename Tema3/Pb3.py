def compare_dex(d1, d2):
    if d1.keys() != d2.keys():
        return False
    
    for k in d1:
        v1 = d1[k]
        v2 = d2[k]

        if isinstance(v1, dict) and isinstance(v2, dict):
            if not compare_dex(v1, v2):
                return False
        elif isinstance(v1, (list, set)) and isinstance(v2, (list, set)):
            if sorted(v1) != sorted(v2):
                return False
        else:
            if v1 != v2:
                return False
    return True

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a': 1, 'b': 2, 'c': 5}
print(compare_dex(d1, d2))