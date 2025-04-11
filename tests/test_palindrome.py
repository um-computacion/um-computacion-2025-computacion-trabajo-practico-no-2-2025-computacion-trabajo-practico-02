import unittest
from src.palindrome import is_palindrome

class TestPalindromeSimples(unittest.TestCase):
    def test_simple_palindromes_1(self):
        self.assertTrue(is_palindrome("oso"))
    def test_simple_palindromes_2(self):
        self.assertTrue(is_palindrome("ana"))
    def test_simple_palindromes_3(self):
        self.assertTrue(is_palindrome("level"))
    def test_simple_palindromes_4(self):
        self.assertTrue(is_palindrome("aa"))
    def test_simple_palindromes_5(self):
        self.assertTrue(is_palindrome("ava"))

if __name__ == '__main__':
    unittest.main()
