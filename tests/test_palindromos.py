import unittest
from src.palindromos import is_palindromo

class TestPalindromo(unittest.TestCase):
    def test_simple_palindromo(self):
        self.assertTrue(is_palindromo("radar"))
        self.assertTrue(is_palindromo("somos"))
        self.assertTrue(is_palindromo("reconocer"))
        self.assertTrue(is_palindromo("rotor"))
        self.assertTrue(is_palindromo("oso"))
#Prueba que estas palabras son palindromos

    def test_simple_no_palindromo(self):
        self.assertFalse(is_palindromo("hola"))
        self.assertFalse(is_palindromo("amor"))
        self.assertFalse(is_palindromo("calculadora"))
        self.assertFalse(is_palindromo("casa"))
        self.assertFalse(is_palindromo("lluvia"))
#Prueba que estas palabras NO son palinromos

    def test_case_insentive(self):
        self.assertTrue(is_palindromo("Radar"))
        self.assertTrue(is_palindromo("Anilina"))
        self.assertTrue(is_palindromo("ReCOnocEr"))
        self.assertTrue(is_palindromo("Amor a Roma"))
        self.assertTrue(is_palindromo("NeuQuen"))
#Prueba que la funcion ignora las mayusculas y las minusculas en las frases y/o palabras

    def test_frase_palindromo(self):
        self.assertTrue(is_palindromo("Amo la pacifica paloma"))
        self.assertTrue(is_palindromo("Isaac no ronca asi "))
        self.assertTrue(is_palindromo("Asi Mario oira misa"))
        self.assertTrue(is_palindromo("Se verlas al reves"))
        self.assertTrue(is_palindromo("Pull up if i pull up"))
#Prueba que estas frases son palindromos

    def test_frase_no_palindromo(self):
        self.assertFalse(is_palindromo("Hola tanto tiempo"))
        self.assertFalse(is_palindromo("No deberia hacerlo"))
        self.assertFalse(is_palindromo("Eso esta brutal"))
        self.assertFalse(is_palindromo("Im the music"))
        self.assertFalse(is_palindromo("It was finally released"))
#Prueba que estas frases NO son palindromos

    def test_ignorar_caracteres_no_alphanumericos(self):
        self.assertTrue(is_palindromo("¿Acaso hubo buhos aca?"))
        self.assertTrue(is_palindromo("No deseo yo ese don."))
        self.assertTrue(is_palindromo("¡Arriba la birra!"))
        self.assertTrue(is_palindromo("A ti no, bonita."))
        self.assertTrue(is_palindromo("A Toyota! Race fast, safe car. A Toyota"))
#Prueba que la funcion ignore los puntos, comas y signos de exclamacion e interrogacion siendo la palabra palindromo

    def test_espacios_ignorar(self):
        self.assertTrue(is_palindromo("never odd or even"))
        self.assertTrue(is_palindromo("  somos o  no somos  "))
        self.assertTrue(is_palindromo("a m o r a r o m a"))
#Prueba que la funcion ignore los espacios en blanco siendo palabras en palindromo 

    def cadenas_vacias(self):
        self.assertFalse(is_palindromo(""))
        self.assertFalse(is_palindromo("c"))
        self.assertFalse(is_palindromo(" "))
        self.assertFalse(is_palindromo(".,;:!?"))
#Prueba casos donde las cadenas son vacios o de un solo caracter

if __name__ == "__main__":
    unittest.main()
