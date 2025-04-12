def is_palindrome(text):
    
    cleaned_text = clean_text(text)

    return compare_characters(cleaned_text)

def clean_text(text):
   
    text = text.lower()

    
    text = text.replace("á", "a").replace("é", "e").replace("í", "i")
    text = text.replace("ó", "o").replace("ú", "u")
    text = text.replace("ü", "u")

    
    cleaned = ""
    for caracter in text:
        if caracter.isalpha():  
            cleaned += caracter

    return cleaned

def compare_characters(cleaned_text):
    
    return cleaned_text == cleaned_text[::-1]

if __name__ == "__main__":
    while True:
        
        frase = input("Ingrese una palabra o frase (o 'salir' para terminar): ")
        
        if frase.lower() == 'salir':  
            print("¡Hasta luego!")
            break

        resultado = is_palindrome(frase)
        
        if resultado == "No se permiten números":
            print("¡Error! No se permiten números.")
        else:
            if resultado:
                print(f'"{frase}" es un palíndromo')
            else:
                print(f'"{frase}" no es un palíndromo')