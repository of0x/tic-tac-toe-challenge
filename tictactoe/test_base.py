from tictactoe import app
from tictactoe.datatbase import init_db, drop_tables

import unittest


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        app.config["DATABASE"] = "sqlite://"
        self.app = app.test_client()
        init_db()
        self.context = app.test_request_context()
        self.context.push()

    def tearDown(self):
        self.context.pop()
        drop_tables()