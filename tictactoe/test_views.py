from tictactoe.test_base import BaseTestCase


import unittest
from flask import json, url_for


class IndexTestCase(BaseTestCase):

    def setUp(self):
        BaseTestCase.setUp(self)
        self.data = dict(firstPlayer='dan')
        self.app.post(url_for("index"),
                      data=json.dumps(self.data), content_type="application/json")

    def test_get_on_index(self):
        response = self.app.get(url_for('index'))
        self.assertEqual(response.status_code, 200)

    def test_posts_to_index_with_empty_json(self):
        response = self.app.post(url_for('index'),
                data=json.dumps(dict()), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_posts_to_index_with_all_fields(self):
        data = dict(firstPlayer='alice', secondPlayer='bob', board='_,1,0,_,_,0,_,_,_')
        response = self.app.post(url_for('index'),
                data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_index_multiple_posts_get(self):
        first = dict(firstPlayer='alice')
        self.app.post(url_for('index'), data=json.dumps(first), content_type='application/json')
        second = dict(firstPlayer='bob')
        self.app.post(url_for('index'), data=json.dumps(second), content_type='application/json')
        third = dict(firstPlayer='charlize')
        self.app.post(url_for('index'), data=json.dumps(third), content_type='application/json')
        response = self.app.get(url_for('index'))
        response_data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_data[0]['firstPlayer'], 'dan') # from setup
        self.assertEqual(response_data[1]['firstPlayer'], first['firstPlayer'])
        self.assertEqual(response_data[2]['firstPlayer'], second['firstPlayer'])
        self.assertEqual(response_data[3]['firstPlayer'], third['firstPlayer'])

    def test_game_allows_get(self):
        response = self.app.get(url_for("game", game_id=1))
        self.assertEqual(response.status_code, 200)

    def test_game_404_on_unfound_id(self):
        response = self.app.get(url_for("game", game_id=9))
        self.assertEqual(response.status_code, 404)

    def test_game_allows_post(self):
        first = dict(firstPlayer='alice')
        self.app.post(url_for("game", game_id=1), data=json.dumps(first), content_type='application/json')
        response = self.app.get(url_for("game", game_id=1))
        response_data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data['firstPlayer'], first['firstPlayer'])

    def test_game_allows_delete(self):
        response = self.app.delete(url_for('game',game_id=1)) # id 1 is in setup
        self.assertEqual(response.status_code, 200)



if __name__ == '__main__':
    unittest.main()
