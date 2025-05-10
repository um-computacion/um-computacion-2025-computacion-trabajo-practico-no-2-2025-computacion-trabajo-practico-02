import unittest
from palindrome import is_palindrome 

class TestPalindromos(unittest.TestCase):
    def test_palabra_simple(self):
        self.assertTrue(is_palindrome("reconocer"))

    def test_con_espacios(self):
        self.assertTrue(is_palindrome("buenas tardes profe quinteros"))

    def test_no_es_palindromo(self):
        self.assertFalse(is_palindrome("race a car"))

    def test_no_es_palindromo(self):
        self.assertFalse(is_palindrome("Mundo"))

if __name__ == '__main__':
    unittest.main()
