def is_palindrome(mystring):
    for indice in range(0, len(mystring)):
        print(f"{mystring[indice]} --> {mystring[-(indice + 1)]}")  
        if mystring[indice] != mystring[-(indice + 1)]:
            print("xno es un palíndromo")
            return False
    return True



