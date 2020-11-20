import unittest

from app import create_app
from config import config


class TaskTest(unittest.TestCase):

    def setUp(self):
        app = create_app(config['test'])
        self.app = app.test_client()
        self.assertEqual(app.debug, False)

    def tearDown(self):
        pass

    def test_index(self):
        response = self.app.get('/api/tasks', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
