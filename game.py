import constants
import copy
import pandas as pd

class Game:

    def __init__(self, player1, player2, board):
        self.player1 = player1
        self.player2 = player2
        self.board = board

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
        playerXWins = 0
        playerOWins = 0
        draws = 0
        numberOfGamesAxis = []
        playerXWinsAxis = []
        playerOWinsAxis = []
        drawsAxis = []
        for i in range(numberOfGames):
            totalWins = playerXWins + playerOWins + draws
            if totalWins > 0:
                self.printStatistics(playerXWins, playerOWins, draws, i + 1)
            self.board.resetBoard()
            self.playGame()
            if self.board.getGameResult() == constants.PLAYER_X_VAL:
                playerXWins = playerXWins + 1
            elif self.board.getGameResult() == constants.PLAYER_O_VAL:
                playerOWins = playerOWins + 1
            else:
                draws = draws + 1
            numberOfGamesAxis.append(i + 1)
            playerXWinsAxis.append(playerXWins)
            playerOWinsAxis.append(playerOWins)
            drawsAxis.append(draws)

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
