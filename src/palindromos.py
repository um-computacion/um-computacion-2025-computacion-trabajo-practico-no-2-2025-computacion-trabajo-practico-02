def is_palindromo(text):
    if text is None or text == "":
        return False
        
    text = text.lower()
    
    clean_text = ""
    for char in text:
        if char.isalnum():
            clean_text += char
    
    if clean_text == "" or (len(clean_text) == 1 and not clean_text.isalnum()):
        return False
    
    return clean_text == clean_text[::-1]

if __name__ == "__main__":
    texto = input("Ingrese palabra o frase: ")
    resultado = is_palindromo(texto)
    if resultado:
        print("Es un palíndromo")
    else:
        print("No es un palíndromo")



   