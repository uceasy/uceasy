import unittest
import web


class UceasyTestCase(unittest.TestCase):

    def setUp(self):
        self.app = web.app.test_client()

    def test_index(self):
        response = self.app.get('/')
        self.assertIn('Welcome to uceasy', response.data.decode())


if __name__ == '__main__':
    unittest.main()
