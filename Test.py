import unittest

from src.palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_simple_palindromes(self):
        self.assertTrue(is_palindrome("reconocer"))
        self.assertTrue(is_palindrome("arenera"))
        self.assertTrue(is_palindrome("salas"))

    def test_palindromes_with_special_characters(self):
        self.assertTrue(is_palindrome("Anita lava la tina"))
        self.assertTrue(is_palindrome("A mamá Roma le aviva el amor a mamá"))
        self.assertTrue(is_palindrome("La sal no sal"));

    def test_non_palindromes(self):
        self.assertFalse(is_palindrome("ejemplo"))
        self.assertFalse(is_palindrome("programacion"))
        self.assertFalse(is_palindrome("palabra"))

    def test_case_insensitivity(self):
        self.assertTrue(is_palindrome("ReConocer"))
        self.assertTrue(is_palindrome("Ana"))
        self.assertTrue(is_palindrome("Oso"))

    def test_edge_cases(self):
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("A"))

if __name__ == '__main__':
    unittest.main()
