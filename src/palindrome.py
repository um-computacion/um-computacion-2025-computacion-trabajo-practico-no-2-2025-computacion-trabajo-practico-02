def limpiar_texto(texto):
    return ''.join(c.lower() for c in texto if c.isalnum())
# este va a elimina espacios, signos y pasar todo a minúsculas

def comparar_textos(original, invertido):
    return original == invertido
# este es el q Compara si el texto limpio es igual a su reverso
def is_palindrome(text):
    # y este es el Usa las funciones auxiliares para verificar si es palíndromo
    cleaned = limpiar_texto(text)
    return comparar_textos(cleaned, cleaned[::-1])
if __name__ == "__main__":
    try:
        while True:
            entrada = input("Ingrese una palabra o frase: ")
            if is_palindrome(entrada):
                print(f'"{entrada}" es un palíndromo')
            else:
                print(f'"{entrada}" no es un palíndromo')
    except KeyboardInterrupt:
        print("\nPrograma finalizado.")
