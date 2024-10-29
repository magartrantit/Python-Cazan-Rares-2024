def loop(mapping):
    result = []
    visited = set()
    curr = mapping['start']

    while curr not in visited:
        visited.add(curr)
        result.append(curr)
        curr = mapping[curr]
    
    return result

mapping = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
result = loop(mapping)
print(result)