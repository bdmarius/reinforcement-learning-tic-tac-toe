import constants
from strategy import Strategy
import copy
import random
import json

class QStrategy(Strategy):

    def __init__(self):
        Strategy.__init__(self, constants.Strategies.Q)
        self.learningRate = 0.2
        self.decay = 0.8
        '''map of (board hash, board)'''
        self.states = {}
        self.states_history = []
        self.exploratory_rate = 0.1


    def selectMove(self, availableMoves, board, playerValue):
        probability = random.uniform(0, 1)
        if probability <= self.exploratory_rate:
            bestMove = availableMoves[random.randrange(0, len(availableMoves))]
        else:
            maxValue = float("-inf")
            bestMove = availableMoves[0]
            for availableMove in availableMoves:
                # get a copy of a board
                boardCopy = copy.deepcopy(board)
                boardCopy[availableMove[0]][availableMove[1]] = playerValue
                value = self.states.get(self.computeHash(boardCopy)) if self.states.get(
                    self.computeHash(boardCopy)) else 0
                if value > maxValue:
                    maxValue = value
                    bestMove = availableMove

        # Remember this state
        boardCopy = copy.deepcopy(board)
        boardCopy[bestMove[0]][bestMove[1]] = playerValue
        self.states_history.append(self.computeHash(boardCopy))
        return bestMove

    def computeHash(self, board):
        """Rearrange the board matrix as a single vector of 9 elements and convert it to string"""
        return str(board)

    def reward(self, rewardValue):
        for stateHash in reversed(self.states_history):
            if self.states.get(stateHash) is None:
                self.states[stateHash] = 0
            self.states[stateHash] += self.learningRate * (self.decay * rewardValue - self.states[stateHash])
            rewardValue = self.states[stateHash]

    def resetStatesHistory(self):
        self.states_history = []


