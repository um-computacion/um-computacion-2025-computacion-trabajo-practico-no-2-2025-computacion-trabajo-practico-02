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
        
    def test_son_robos_o_sobornos(self):
        resultado = is_palindrome("son robos o sobornos")
        self.assertEqual(resultado, True)

    def test_anita_lava_la_tina(self):
        resultado = is_palindrome("anita lava la tina")
        self.assertEqual(resultado, True) 

    def test_amo_la_pacifica_paloma(self):  
        resultado = is_palindrome("amo la pacifica paloma")
        self.assertEqual(resultado, True)
    
    def test_casa(self):
        resultado = is_palindrome("casa")
        self.assertEqual(resultado, False)

    def test_programacion(self):
        resultado = is_palindrome("programacion")
        self.assertEqual(resultado, False)

    def test_esto_no_es_palindromo(self):
        resultado = is_palindrome("esto no es palindromo")
        self.assertEqual(resultado, False)

    def test_me_gusta_python(self):
        resultado = is_palindrome("me gusta python")
        self.assertEqual(resultado, False)

    def test_el_sol_no_esta(self):
        resultado = is_palindrome("el sol no está")
        self.assertEqual(resultado, False)

if __name__ == '__main__':
    unittest.main()


     