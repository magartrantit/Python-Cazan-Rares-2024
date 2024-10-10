def camel_to_underscore(str):
    ct = 0
    for i in str:
        if i.isupper() and ct != 0:
            str = str.replace(i, "_" + i.lower())
        elif i.isupper() and ct == 0:
            str = str.replace(i, i.lower())
            ct = ct + 1  
    return str

input_str = input("Dati un string UpperCamelCase: ")
print("Lowercase_with_underscores: ", camel_to_underscore(input_str))