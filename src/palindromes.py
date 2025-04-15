import unicodedata

def is_palindrome(text):

    text = ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    )
    text = text.lower()
    text = ''.join(c for c in text if c.isalnum())
    return text == text[::-1]