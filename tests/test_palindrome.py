import unittest
from src.palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_simple_palindromes(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome("anita lava la tina"))
        self.assertTrue(is_palindrome("dábale arroz a la zorra el abad"))
        self.assertTrue(is_palindrome("¿Acaso hubo búhos acá?"))
        self.assertTrue(is_palindrome("reconocer"))
        self.assertTrue(is_palindrome("oso"))
        self.assertFalse(is_palindrome("palabra"))
        self.assertFalse(is_palindrome("no es un palindromo"))

if __name__ == '__main__':
    unittest.main()

from src.palindrome import clean_text

class TestCleanText(unittest.TestCase):

    def test_clean_text(self):
        self.assertEqual(clean_text("A man, a plan, a canal, Panama!"), "amanaplanacanalpanama")
        self.assertEqual(clean_text("No 'x' in Nixon"), "noxinnixon")
        self.assertEqual(clean_text("Madam, in Eden, I'm Adam"), "madaminedenimadam")
        self.assertEqual(clean_text("¡Hola!"), "hola")
        self.assertEqual(clean_text("¿Acaso hubo búhos acá?"), "acasohubobuhosaca")

if __name__ == "__main__":
    unittest.main()