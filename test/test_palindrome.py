import unittest
from src.palindrome import is_palindrome  # Este import puede fallar al principio, está bien así

class TestPalindrome(unittest.TestCase):
    def test_simple_palindromes(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("level"))

    def test_frases_palindromas(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertTrue(is_palindrome("Anita lava la tina"))
        self.assertTrue(is_palindrome("La ruta natural"))

    def test_no_palindromos(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("python"))
        self.assertFalse(is_palindrome("computadora"))

    def test_casos_edge(self):
        self.assertTrue(is_palindrome(""))  
        self.assertTrue(is_palindrome("a")) 
        self.assertTrue(is_palindrome("A")) 
        self.assertTrue(is_palindrome("12321"))  
        self.assertTrue(is_palindrome("123321"))
        self.assertFalse(is_palindrome("12345"))

if __name__ == "__main__":
    unittest.main()
