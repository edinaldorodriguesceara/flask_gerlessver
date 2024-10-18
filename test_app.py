import unittest
from app import app  # Substitua 'your_flask_app' pelo nome do seu arquivo, sem a extensão .py

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        """Configura a aplicação para os testes."""
        self.app = app.test_client()
        self.app.testing = True

    def test_hello_world(self):
        """Teste se a rota / retorna 'Hello World!'"""
        response = self.app.get('/')
        self.assertEqual(response.data.decode(), 'Hello World!')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
