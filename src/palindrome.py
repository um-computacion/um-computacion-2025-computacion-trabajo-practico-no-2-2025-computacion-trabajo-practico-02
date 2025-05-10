
def is_palindrome(texto):

    texto_limpio = limpiar_texto(texto)

    return comparar(texto_limpio) 

def limpiar_texto(texto):
    
    texto = texto.lower()
    limpio = ""
    for caracter in texto:
        if caracter.isalnum():
            limpio += caracter
    return limpio