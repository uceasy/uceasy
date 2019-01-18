import unittest

import uceasy


class UceasyTestCase(unittest.TestCase):

    def setUp(self):
        self.app = uceasy.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertIn('Welcome to uceasy', rv.data.decode())


if __name__ == '__main__':
    unittest.main()
