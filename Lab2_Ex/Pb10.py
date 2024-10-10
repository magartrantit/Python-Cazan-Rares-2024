def invert_sentence(s):
    words = s.split()
    return ' '.join(words[::-1])

s = input("Dati sirul: ")
print(invert_sentence(s))