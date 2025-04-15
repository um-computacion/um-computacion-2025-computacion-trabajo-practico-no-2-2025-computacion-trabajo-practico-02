import unittest

from src.palindromo import is_palindromo

class TestPalindromo(unittest.TestCase):
    def test_simple_palindromo(self):
        self.assertTrue(is_palindromo("radar"))
        self.assertTrue(is_palindromo("somos"))
        self.assertTrue(is_palindromo("reconocer"))
        self.assertTrue(is_palindromo("rotor"))
        self.assertTrue(is_palindromo("oso"))
    
    def test_frase_palindromo(self):
        self.assertTrue(is_palindromo("Amo la pacifica paloma"))
        self.assertTrue(is_palindromo("Isaac no ronca asi "))
        self.assertTrue(is_palindromo("Asi Mario oira misa"))
        self.assertTrue(is_palindromo("Se verlas al reves"))
        self.assertTrue(is_palindromo("Pull up if i pull up"))
    
    def test_simple_no_palindromo(self):
        self.assertFalse(is_palindromo("hola"))
        self.assertFalse(is_palindromo("amor"))
        self.assertFalse(is_palindromo("calculadora"))
        self.assertFalse(is_palindromo("casa"))
        self.assertFalse(is_palindromo("lluvia"))
    
    def test_frase_no_palindromo(self):
        self.assertFalse(is_palindromo("Hola tanto tiempo"))
        self.assertFalse(is_palindromo("No deberia hacerlo"))
        self.assertFalse(is_palindromo("Eso esta brutal"))
        self.assertFalse(is_palindromo("Im the music"))
        self.assertFalse(is_palindromo("It was finally released"))
    
    def test_ignorar_caracteres_no_alphanumericos(self):
        self.assertTrue(is_palindromo("¿Acaso hubo buhos aca?"))
        self.assertTrue(is_palindromo("No deseo yo ese don."))
        self.assertTrue(is_palindromo("¡Arriba la birra!"))
        self.assertTrue(is_palindromo("A ti no, bonita."))
        self.assertTrue(is_palindromo("A Toyota! Race fast, safe car. A Toyota"))

    def test_espacios_ignorar(self):
        self.assertTrue(is_palindromo("never odd or even"))
        self.assertTrue(is_palindromo(" somos o no somos "))
        self.assertTrue(is_palindromo("a m o r a r o m a"))

    def cadenas_vacias(self):
        self.assertFalse(is_palindromo(""))
        self.assertFalse(is_palindromo("c"))
        self.assertFalse(is_palindromo(" "))
        self.assertFalse(is_palindromo(".,;:!?"))

if __name__ == "__main__":
    unittest.main()
#

