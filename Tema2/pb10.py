def combine_lists(*args):
    max_length = max(len(lst) for lst in args)
    result = []
    
    for i in range(max_length):
        tuple_elements = tuple(lst[i] if i < len(lst) else None for lst in args)
        result.append(tuple_elements)
    
    return result

list1 = [1, 2, 3]
list2 = [5, 6, 7]
list3 = ["a", "b", "c"]
print(combine_lists(list1, list2, list3))