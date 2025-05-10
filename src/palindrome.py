import re

def is_palindrome(mystring):
    
    mystring = re.sub(r'[^a-zA-Z0-9]', '', mystring.lower())

    for indice in range(0, len(mystring)):
        print(mystring[indice] + " --> " + mystring[-(indice + 1)])
        if mystring[indice] != mystring[-(indice + 1)]:
            print("No es un palíndromo")
            return False
    print("Es un palíndromo")
    return True


if __name__ == "__main__":
    entrada = input("Ingresá una palabra o frase: ")
    is_palindrome(entrada)



