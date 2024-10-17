def aparente(*args, x):
    ret_list = []
    combined_list = []
    for i in args:
        combined_list.extend(i)
    for i in range(len(combined_list)):
        if combined_list.count(i) == x:
            ret_list += [i]
    return ret_list

print(aparente([1,2,3], [2,3,4],[4,5,6], [4,1, "test"], x = 2))