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


    def test_phrase_palindromes_1(self):
        self.assertTrue(is_palindrome("Anita lava la tina"))
    def test_phrase_palindromes_2(self):
        self.assertTrue(is_palindrome("A ti no, bonita"))
    def test_phrase_palindromes_3(self):
        self.assertTrue(is_palindrome("No lemon, no melon"))
    def test_phrase_palindromes_4(self):
        self.assertTrue(is_palindrome("La sal, a la sala"))
    def test_phrase_palindromes_5(self):
        self.assertTrue(is_palindrome("La ruta natural"))
    def test_phrase_palindromes_6(self):
        self.assertTrue(is_palindrome("Yo dono rosas, oro no doy"))

if __name__ == '__main__':
    unittest.main()
