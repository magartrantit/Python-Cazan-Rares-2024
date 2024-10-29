def operations(*args):
    sets = [set(arg) for arg in args]
    result = {}
    for i in sets:
        for j in sets:
            if i != j:
                result[f'{i} and {j}'] = [i.intersection(j)]
                result[f'{i} or {j}'] = [i.union(j)]
                result[f'{i} - {j}'] = [i.difference(j)]
                result[f'{j} - {i}'] = [j.difference(i)]
    return result

s1 = [1, 2, 3]
s2 = [3, 4, 5]
s3 = [5, 6, 7]
print(operations(s1, s2, s3))