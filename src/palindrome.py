def is_palindrome(texto):
    # pasar a minus
    texto = texto.lower()
    
    # eliminar espacios
    texto = texto.replace(" ", "")
    
    # comparar con el reverso
    return texto == texto[::-1]

if __name__ == "__main__": ...