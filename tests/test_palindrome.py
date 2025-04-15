import unittest
from src.palindrome import is_palindrome

class TestPalindromos(unittest.TestCase):
    
    def test_palindromos_en_minusculas(self):

        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("salas"))
        self.assertTrue(is_palindrome("oso"))
        self.assertTrue(is_palindrome("radar"))
        
    def test_frases_palindromas(self):
        self.assertTrue(is_palindrome("Dábale arroz a la zorra el abad"))
        self.assertTrue(is_palindrome("A mamá Roma le aviva el amor a mamá"))
        self.assertTrue(is_palindrome("Anita lava la tina"))
        
if __name__ == '__main__':
    unittest.main()