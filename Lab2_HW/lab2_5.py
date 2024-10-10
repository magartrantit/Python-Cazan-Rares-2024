nr = input("Dati un numar: ")
def is_palindrome(nr):
    if nr == nr[::-1]:
        return True
    else:
        return False
    
if is_palindrome(nr):
    print("Numarul este palindrom")
else:    
    print("Numarul nu este palindrom")