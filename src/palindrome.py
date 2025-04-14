import re

def is_palindrome(text):
    # Caso especial: texto vacío o un solo carácter es palíndromo
    if len(text) <= 1:
        return True
    
    # Convertir a minúsculas y eliminar caracteres no alfanuméricos
    clean_text = re.sub(r'[^a-zA-Z0-9]', '', text.lower())
    
    # Verificar si es palíndromo comparando con su reverso
    return clean_text == clean_text[::-1]