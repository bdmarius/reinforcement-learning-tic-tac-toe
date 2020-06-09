import constants
import copy
import os

class Board:

    def __init__(self):
        self.board = []
        self.resetBoard()

    def resetBoard(self):
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

    def getGameResult(self):
        # Rows
        for i in range(len(self.board)):
            rowSet = set(self.board[i])
            if len(rowSet) == 1 and self.board[i][0] != 0:
                return self.board[i][0]

        # Columns
        for i in range(len(self.board)):
            column = []
            for j in range(len(self.board[i])):
                column.append(self.board[j][i])
            columnSet = set(column)
            if len(columnSet) == 1 and self.board[0][i] != 0:
                return self.board[0][i]

        # First diagonal
        diagonal = []
        for i in range(len(self.board)):
            diagonal.append(self.board[i][i])
        if len(set(diagonal)) == 1 and self.board[0][0] != 0:
            return self.board[0][0]

        # Second diagonal
        diagonal = []
        for i in range(len(self.board)):
            diagonal.append(self.board[i][len(self.board) - i - 1])
        if len(set(diagonal)) == 1 and self.board[0][2] != 0:
            return self.board[0][2]

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == constants.EMPTY_VAL:
                    return constants.GAME_STATE_NOT_ENDED

        return constants.GAME_STATE_DRAW

    def getAvailableMoves(self):
        availableMoves = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if (self.board[i][j]) == constants.EMPTY_VAL:
                    availableMoves.append([i, j])
        return availableMoves

    def move(self, position, value):
        availableMoves = self.getAvailableMoves()
        for i in range(len(availableMoves)):
            if position[0] == availableMoves[i][0] and position[1] == availableMoves[i][1]:
                self.board[position[0]][position[1]] = value

    def getBoardCopy(self):
        return copy.deepcopy(self.board)

    def printBoard(self):
        print(constants.VERTICAL_SEPARATOR)
        for i in range(len(self.board)):
            print(' ', end='')
            for j in range(len(self.board[i])):
                if constants.PLAYER_X_VAL == self.board[i][j]:
                    print(constants.PLAYER_X, end='')
                elif constants.PLAYER_O_VAL == self.board[i][j]:
                    print(constants.PLAYER_O, end='')
                elif constants.EMPTY_VAL == self.board[i][j]:
                    print(constants.EMPTY, end='')
                print(constants.HORIZONTAL_SEPARATOR, end='')
            print(os.linesep)
            print(constants.VERTICAL_SEPARATOR)