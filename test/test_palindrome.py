import unittest
from src.palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_simple_palindromes(self):
        self.assertTrue(is_palindrome("reconocer"))
        self.assertTrue(is_palindrome("solos"))
        self.assertTrue(is_palindrome("rallar"))

    def test_phrase_palindromes(self):
        self.assertTrue(is_palindrome("amo, la paloma!"))
        self.assertTrue(is_palindrome("amor a roma"))
        self.assertTrue(is_palindrome("atar a la rata"))

    def test_non_palindromes(self):
        self.assertFalse(is_palindrome("juan pablo"))
        self.assertFalse(is_palindrome("argentina"))
        self.assertFalse(is_palindrome("messi"))

    #def test_edge_cases(self):
        #self.assertTrue(is_palindrome(""))
        #self.assertTrue(is_palindrome("a"))
        #self.assertTrue(is_palindrome("A"))

if __name__ == '__main__':
    unittest.main()