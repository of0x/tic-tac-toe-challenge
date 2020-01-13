from tictactoe.datatbase import Base
from sqlalchemy import Column, Integer, String

class Game(Base):

    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    firstPlayer = Column(String)
    secondPlayer = Column(String)
    board = Column(String)

    EMPTY_BOARD = '_,_,_,_,_,_,_,_,_'

    def __init__(self, firstPlay=None, secondPlayer=None, board=EMPTY_BOARD):
        self.firstPlayer = firstPlay
        self.secondPlayer = secondPlayer
        self.board = board

    def __repr__(self):
        return 'game: {} player1: {} player2: {} boardState: {}'\
            .format(self.id, self.firstPlayer, self.secondPlayer, self.board )

