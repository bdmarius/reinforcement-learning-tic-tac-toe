import abc

class Strategy:

    def __init__(self, type):
        self.type = type

    @abc.abstractmethod
    def selectMove(self,  availableMoves, board, playerValue):
        """Select a move from the list of available moves"""

    @abc.abstractmethod
    def reward(self, rewardValue):
        """Applicable only for Q Strategy"""

    @abc.abstractmethod
    def resetStatesHistory(self):
        """Applicable only for Q Strategy """