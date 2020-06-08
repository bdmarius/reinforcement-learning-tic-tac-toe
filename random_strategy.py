from strategy import Strategy
import random
import constants

class RandomStrategy(Strategy):

    def __init__(self):
        Strategy.__init__(self, constants.Strategies.RANDOM)

    def selectMove(self, availableMoves, board, playerValue):
        return availableMoves[random.randrange(0, len(availableMoves))]