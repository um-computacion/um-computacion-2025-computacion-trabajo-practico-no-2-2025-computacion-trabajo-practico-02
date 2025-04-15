import unittest

from src.palindromo import is_palindromo

class TestPalindromo(unittest.TestCase):
    def test_simple_palindromo(self):
        self.assertTrue(is_palindromo("radar"))
        self.assertTrue(is_palindromo("somos"))
        self.assertTrue(is_palindromo("reconocer"))
        self.assertTrue(is_palindromo("rotor"))
        self.assertTrue(is_palindromo("oso"))
    
    def test_frase_palindromo(self):
        self.assertTrue(is_palindromo("Amo la pacifica paloma"))
        self.assertTrue(is_palindromo("Isaac no ronca asi "))
        self.assertTrue(is_palindromo("Asi Mario oira misa"))
        self.assertTrue(is_palindromo("Se verlas al reves"))
        self.assertTrue(is_palindromo("Pull up if i pull up"))

