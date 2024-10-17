def get_third_char(tup):
    return tup[1][2]

def order(tuple_list):
    return sorted(tuple_list, key=get_third_char)

tuple_list = [('abc', 'bcd'), ('abc', 'zza')]
print(order(tuple_list))  