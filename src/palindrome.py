def limpiar_texto(texto):
    return ''.join(c.lower() for c in texto if c.isalnum())

def is_palindrome(text):
    # Esta funcion en es la que eliminara los espacios y pasara todo a minúsculas
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]
