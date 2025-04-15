from src.palindrome import is_palindrome
import unittest


class TestPalindrome(unittest.TestCase):

    def test_a(self):
        resultado = is_palindrome("a")
        self.assertEqual(resultado, True)

    def test_aa(self):
        resultado = is_palindrome ("aa")
        self.assertEqual(resultado,(True))
  
    def test_as(self):
        resultado = is_palindrome ("oso")
        self.assertEqual(resultado, True)

    def test_ana(self):
        resultado = is_palindrome("ana")
        self.assertEqual(resultado, True)

    def test_salas(self):
        resultado = is_palindrome("salas")
        self.assertEqual(resultado, True)

    def test_neuquen(self):
        resultado = is_palindrome('neuquen')
        self.assertEqual(resultado, True)
    
if __name__ == '__main__':
    unittest.main()


     