import re

def is_palindrome(text):
    # Eliminar todo lo que no sea letra o número
    cleaned = re.sub(r'[^A-Za-z0-9]', '', text)
    # Pasar a minúsculas
    cleaned = cleaned.lower()
    # Comparar con su reverso
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    while True:
        try:
            entrada = input("Ingrese una palabra o frase: ")
            if is_palindrome(entrada):
                print(f'"{entrada}" es un palíndromo\n')
            else:
                print(f'"{entrada}" no es un palíndromo\n')
        except KeyboardInterrupt:
            print("\nPrograma finalizado.")
            break
