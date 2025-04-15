import re

def is_palindrome(text):

    text = text.lower()
    
    text = re.sub(r'[^a-záéíóúüñ]', '', text)
    
    return text == text[::-1]


