import constants
import copy
import pandas as pd

class Game:

    def __init__(self, player1, player2, board):
        self.player1 = player1
        self.player2 = player2
        self.board = board
        self.playerXWins = 0
        self.playerOWins = 0
        self.draws = 0

    def playGame(self):
        playerToMove = self.player1
        while (self.board.getGameResult() == constants.GAME_STATE_NOT_ENDED):
            availableMoves = self.board.getAvailableMoves()
            selectedMove = playerToMove.move(availableMoves, copy.deepcopy(self.board.getBoardCopy()))
            self.board.move(selectedMove, playerToMove.getValue())
            if playerToMove == self.player1:
                playerToMove = self.player2
            else:
                playerToMove = self.player1
        if self.board.getGameResult() == self.player1.getValue():
            self.player1.reward(1)
            self.player2.reward(-1)
        elif self.board.getGameResult() == self.player2.getValue():
            self.player1.reward(-1)
            self.player2.reward(1)
        else:
            self.player1.reward(0.1)
            self.player2.reward(0.1)

        self.player1.resetStatesHistory()
        self.player2.resetStatesHistory()

    def playManyGames(self, numberOfGames):
        self.playerXWins = 0
        self.playerOWins = 0
        self.draws = 0
        numberOfGamesAxis = []
        playerXWinsAxis = []
        playerOWinsAxis = []
        drawsAxis = []
        for i in range(numberOfGames):
            totalWins = self.playerXWins + self.playerOWins + self.draws
            if totalWins > 0:
                self.printStatistics(self.playerXWins, self.playerOWins, self.draws, i + 1)
            self.board.resetBoard()
            self.playGame()
            if self.board.getGameResult() == constants.PLAYER_X_VAL:
                self.playerXWins = self.playerXWins + 1
            elif self.board.getGameResult() == constants.PLAYER_O_VAL:
                self.playerOWins = self.playerOWins + 1
            else:
                self.draws = self.draws + 1
            numberOfGamesAxis.append(i + 1)
            playerXWinsAxis.append(self.playerXWins)
            playerOWinsAxis.append(self.playerOWins)
            drawsAxis.append(self.draws)

        statistics = {"Games": numberOfGamesAxis,
                     "X": playerXWinsAxis,
                     "O": playerOWinsAxis,
                     "Draws": drawsAxis}
        return pd.DataFrame(statistics, columns = ['Games', 'X', 'O', 'Draws'])

    def printStatistics(self, playerXWins, playerOWins, draws, numberOfGames):
        print ("Number of games: {}".format(numberOfGames))
        totalWins = playerXWins + playerOWins + draws
        print('X Wins: {} ({}%)'.format(str(playerXWins), str(int(playerXWins * 100 / totalWins))))
        print('O Wins: {} ({}%)'.format(str(playerOWins), str(int(playerOWins * 100 / totalWins))))
        print('Draws:  {} ({}%)'.format(str(draws), str(int(draws * 100 / totalWins))))

    def printFinalStatistics(self):
        totalWins = self.playerXWins + self.playerOWins + self.draws
        print('X Wins: {} ({}%)'.format(str(self.playerXWins), str(int(self.playerXWins * 100 / totalWins))))
        print('O Wins: {} ({}%)'.format(str(self.playerOWins), str(int(self.playerOWins * 100 / totalWins))))
        print('Draws:  {} ({}%)'.format(str(self.draws), str(int(self.draws * 100 / totalWins))))
