

class Player:

    def __init__(self, value, strategy):
        self.value = value
        self.strategy = strategy

    def getValue(self):
        return self.value

    def move(self, availableMoves, board):
        return self.strategy.selectMove(availableMoves, board, self.value)

    def reward(self, rewardValue):
        self.strategy.reward(rewardValue)

    def resetStatesHistory(self):
        self.strategy.resetStatesHistory()
