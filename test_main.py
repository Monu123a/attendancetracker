import unittest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestAPI(unittest.TestCase):
    def test_health(self):
        response = client.get('/health')
        self.assertEqual(response.status_code, 200)
    def test_invalid_register(self):
        response = client.post('/register')
        self.assertEqual(response.status_code, 422)
    def test_invalid_recognize(self):
        response = client.post('/recognize')
        self.assertEqual(response.status_code, 422)

if __name__ == '__main__':
    unittest.main()
