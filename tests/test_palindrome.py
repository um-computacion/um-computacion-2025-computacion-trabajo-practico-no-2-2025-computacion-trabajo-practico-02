from src.palindrome import is_palindrome
import unittest

class TestPalindrome(unittest.TestCase):
    def test_a(self):
        resultado = is_palindrome("AcA")
        self.assertEqual(resultado, True)

    def test_b(self):
        resultado = is_palindrome("ABCA")
        self.assertEqual(resultado, False)
 

if __name__ == '__main__':
    unittest.main()