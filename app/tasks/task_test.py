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

    def test_get_task_by_id(self):
        response = self.app.get('/api/tasks/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_get_task_not_found(self):
        response = self.app.get('/api/tasks/1000', follow_redirects=True)
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
