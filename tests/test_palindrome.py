import unittest

def palindromo(texto):
    texto = texto.lower()
    
    solo_letras = ""
    for caracter in texto:
        if caracter.isalnum(): 
            solo_letras += caracter
    
    return solo_letras == solo_letras[::-1]

class TestPalindrome(unittest.TestCase):
    def test_simple_palindromes(self):
        self.assertTrue(palindromo("madam"))
        self.assertTrue(palindromo("racecar"))
        self.assertTrue(palindromo("level"))
        
    def test_phrase_palindromes(self):
        self.assertTrue(palindromo("A man, a plan, a canal: Panama"))
        self.assertTrue(palindromo("Was it a car or a cat I saw?"))
        self.assertTrue(palindromo("No lemon, no melon"))
        
    def test_non_palindromes(self):
        self.assertFalse(palindromo("hello"))
        self.assertFalse(palindromo("python"))
        self.assertFalse(palindromo("This is not a palindrome"))
        
    def test_edge_cases(self):
        self.assertTrue(palindromo(""))
        self.assertTrue(palindromo("a"))
        self.assertTrue(palindromo("A"))
        
if __name__ == '__main__':
    unittest.main()