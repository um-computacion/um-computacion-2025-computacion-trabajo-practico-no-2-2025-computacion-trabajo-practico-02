import unittest

class Test_is_palindrome(unittest.TestCase):
    def simple_palindrome_1(self):
        self.assertEqual(is_palindrome('neuquen'),True) 
    def simple_palindrome_2(self):
        self.assertEqual(is_palindrome('ana'),True) 
    def simple_palindrome_3(self):
        self.assertEqual(is_palindrome('otto'),True) 
    def polindrom_phrase_1(self):
        self.assertEqual(is_palindrome('Anita lava la tina'),True)
    def polindrom_phrase_2(self):
        self.assertEqual(is_palindrome('Yo hago yoga hoy'),False)
    def polindrom_phrase_3(self):
        self.assertEqual(is_palindrome('Aman a Panama'),True)
    def no_palindrome_1(self):
        self.assertEqual(is_palindrome('Hola mundo como anda'),False)
    def no_palindrome_2(self):
        self.assertEqual(is_palindrome('botella'),False)
    def no_palindrome_3(self):
        self.assertEqual(is_palindrome('rusia'),False)



        