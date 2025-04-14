import re
import unicodedata

def clean_text(text):
    # Convertir todo a minúsculas
    text = text.lower()
    
    # Eliminar acentos (normalización Unicode)
    text = unicodedata.normalize('NFD', text)
    text = ''.join([c for c in text if unicodedata.category(c) != 'Mn'])
    
    # Eliminar espacios y signos de puntuación usando una expresión regular
    text = re.sub(r'[^a-z0-9]', '', text)
    
    return text

def is_palindrome(text):
    # Limpiar el texto
    cleaned_text = clean_text(text)
    
    # Comparar el texto con su reverso
    return cleaned_text == cleaned_text[::-1]
