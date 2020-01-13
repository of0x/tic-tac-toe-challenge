from tictactoe.test_base import BaseTestCase
from tictactoe.models import Game

from tictactoe.datatbase import db_session


class GameTestCase(BaseTestCase):
    def test_row_creation_with_empty_ctor(self):
        entry = Game()
        db_session.add(entry)
        db_session.commit()
        query = Game.query.all()[0]
        self.assertEqual(str(query), str(entry))

    def test_all_fields_created_and_queriable(self):
        expected_first_player = 'First'
        expected_second_player = 'Second'
        expected_board = '_,1,0,_,_,0,_,_,_'
        entry = Game(expected_first_player, expected_second_player, expected_board)
        db_session.add(entry)
        db_session.commit()
        query = Game.query.filter(Game.firstPlayer == expected_first_player).first()
        self.assertEqual(entry, query, 'mismatched first player')
        query = Game.query.filter(Game.secondPlayer == expected_second_player).first()
        self.assertEqual(entry, query, 'mismatched second player')
        query = Game.query.filter(Game.board == expected_board).first()
        self.assertEqual(entry, query, 'mismatched board')

