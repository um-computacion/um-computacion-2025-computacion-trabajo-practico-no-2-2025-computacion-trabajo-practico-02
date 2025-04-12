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

    def test_non_palindromes_1(self):
        self.assertFalse(is_palindrome("la chica baila"))  
    def test_non_palindromes_2(self):
            self.assertFalse(is_palindrome("mundo"))  
    def test_non_palindromes_3(self):
        self.assertFalse(is_palindrome("esto no es un palíndromo"))  
    def test_non_palindromes_4(self):
        self.assertFalse(is_palindrome("perro"))  
    def test_non_palindromes_5(self):
        self.assertFalse(is_palindrome("mirando la luna"))  
    def test_non_palindromes_6(self):
        self.assertFalse(is_palindrome("a mamá")) 


    def test_casos_edge_1(self):
        self.assertTrue(is_palindrome(""))  
    def test_casos_edge_2(self):
        self.assertTrue(is_palindrome("¡Feliz Cumpleaños!"))  
    def test_casos_edge_3(self):
        self.assertTrue(is_palindrome("A"))  
    def test_casos_edge_4(self):
        self.assertTrue(is_palindrome("aa"))
    def test_casos_edge_5(self):
        self.assertTrue(is_palindrome("¿Cómo estás?"))
           

if __name__ == '__main__':
    unittest.main()
