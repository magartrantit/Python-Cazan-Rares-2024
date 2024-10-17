def div(x=1, list=[], flag=True):
    ret_list = []
    for word in list:
        cuv = []
        for char in word:
            ascii_value = ord(char)
            if(ascii_value % x == 0 and flag) or (ascii_value % x != 0 and not flag):
                cuv.append(char)
        ret_list.append(cuv)
    return ret_list

print(div(2, ["test", "hello", "lab002"], False))   