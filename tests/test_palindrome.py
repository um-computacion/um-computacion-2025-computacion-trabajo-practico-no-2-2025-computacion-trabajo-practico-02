import unittest
from src.palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_simple_palindromes(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("reconocer"))
        self.assertTrue(is_palindrome("level"))
    
    def test_phrase_palindromes(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(is_palindrome("Adan salta y Atlas nada"))
        self.assertTrue(is_palindrome("Sometamos o matemos"))

if __name__ == '__main__':
    unittest.main()