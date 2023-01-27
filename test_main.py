import unittest
from flask_app import app
import model as md 

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_hello(self):
        response = self.app.get('/api/hello')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'hello': 'world'})

    def test_hello_name(self):
        response = self.app.get('/api/hello/ben')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'hello': 'ben'})

    def test_whoami(self):
        response = self.app.get('/api/whoami')
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json['ip'])

    def test_whoami_name(self):
        response = self.app.get('/api/whoami/ben')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], 'ben')




    def test_classifier(self):
        response = self.app.get('/api/classify', query_string=md.classifier)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["prediction"], md.testImgLabel)

if __name__ == '__main__':
    unittest.main()
