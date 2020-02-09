import unittest
from users.models import Person

class TestAutentication(unittest.TestCase):
    """1er caso de prueba:
    Log in de un usuario
    Tener los campos y poder insertar cosas"""
    def testLoginBase1(self):
        Person.objects.create(email="hola", password="hi")
        self.assertTrue(True)

if __name__ == '__main__':
	unittest.main()
