import unittest
from src.palindromes import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_palindrome(self):
        self.assertEqual(is_palindrome("Neuquen"), True)
        self.assertEqual(is_palindrome("Radar"), True)
        self.assertEqual(is_palindrome("Ana"), True)

    def test_palindrome2(self):
        self.assertEqual(is_palindrome("Eve"), True)
        self.assertEqual(is_palindrome("Reviver"), True)
        self.assertEqual(is_palindrome("Ojo rojo"), True)

    def test_palindrome3(self):
        self.assertEqual(is_palindrome("Ala"), True)
        self.assertEqual(is_palindrome("Oso"), True)
        self.assertEqual(is_palindrome("Ama"), True)

if __name__ == "__main__":
    unittest.main()