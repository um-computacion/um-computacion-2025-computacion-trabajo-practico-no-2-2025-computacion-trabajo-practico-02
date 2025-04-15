import unittest

from src.palindromo import is_palindromo

class TestPalindromo(unittest.TestCase):
    def test_simple_palindromo(self):
        self.assertTrue(is_palindromo("radar"))
        self.assertTrue(is_palindromo("somos"))
        self.assertTrue(is_palindromo("reconocer"))
        self.assertTrue(is_palindromo("rotor"))
        self.assertTrue(is_palindromo("oso"))
