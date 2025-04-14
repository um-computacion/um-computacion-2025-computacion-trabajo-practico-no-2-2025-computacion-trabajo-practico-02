import string

def is_palindrome(text):
    # Convertimos a minúsculas
    text = text.lower()

    # Eliminamos caracteres que no son letras ni números
    allowed = string.ascii_lowercase + string.digits
    cleaned = ''.join(char for char in text if char in allowed)

    # Comparamos con su reverso
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    try:
        while True:
            frase = input("Ingrese una palabra o frase: ")
            if is_palindrome(frase):
                print(f'"{frase}" es un palíndromo')
            else:
                print(f'"{frase}" no es un palíndromo')
    except KeyboardInterrupt:
        print("\nSaliendo del programa...")
