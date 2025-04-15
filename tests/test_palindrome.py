from src.palindrome import is_palindrome
import unittest

class TestPalindrome(unittest.TestCase):
    def test_a(self):
        resultado = is_palindrome("AcA")
        self.assertEqual(resultado, True)

    def test_b(self):
        resultado = is_palindrome("ABCA")
        self.assertEqual(resultado, False)

    def test_c(self):
        resultado = is_palindrome("ne  Uq uE n")
        self.assertEqual(resultado, True)

    def test_d(self):
        resultado = is_palindrome("ne uqu     en")
        self.assertEqual(resultado, True)

    def test_e(self):
        resultado = is_palindrome("Anita lava la tina")
        self.assertEqual(resultado, True)
    

    def test_f(self):
        resultado = is_palindrome("Jose")
        self.assertEqual(resultado, False)



    def test_g(self):
        resultado = is_palindrome("Mauro come comida")
        self.assertEqual(resultado, False)     

if __name__ == '__main__':
    unittest.main()