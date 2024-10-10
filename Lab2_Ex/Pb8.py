def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def find_index(word, alphabet):
    length = len(word)
    alphabet = sorted(alphabet)
    factorials = [factorial(i) for i in range(length + 1)]
    
    index = 0
    for i, char in enumerate(word):
        position = alphabet.index(char)
        index += position * factorials[length - i - 1]
        alphabet.pop(position)
    
    return index + 1

word = "defhim"
alphabet = "AEGIJLNOPSUVbdefhimnoprstuvwxy"
print(find_index(word, alphabet))