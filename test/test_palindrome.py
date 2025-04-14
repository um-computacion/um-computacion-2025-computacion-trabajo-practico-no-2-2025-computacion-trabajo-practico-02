import unittest
from src.palindrome import is_palindrome  # este importará después, por ahora puede fallar

class TestPalindrome(unittest.TestCase):
    def test_simple_palindromes(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("level"))

def test_frases_palindromas(self):
    self.assertTrue(is_palindrome("A man a plan a canal Panama"))
    self.assertTrue(is_palindrome("Anita lava la tina"))
    self.assertTrue(is_palindrome("La ruta natural"))
