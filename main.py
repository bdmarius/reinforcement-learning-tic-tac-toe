from random_strategy import RandomStrategy
from q_strategy import QStrategy
from player import Player
import constants
from board import Board
from game import Game
import matplotlib.pyplot as plt

if __name__=="__main__":

    print ("Game 1 - Random vs Random")
    player1Strategy = RandomStrategy()
    player2Strategy = RandomStrategy()
    player1 = Player(constants.PLAYER_X_VAL, player1Strategy)
    player2 = Player(constants.PLAYER_O_VAL, player2Strategy)
    board1 = Board()
    game1 = Game(player1, player2, board1)
    df = game1.playManyGames(1000)
    df.plot(x="Games", y=["X", "O", "Draws"], title="X - Random; O - Random")
    df.plot(x="Games", y=["X", "O", "Draws"])

    print("Game 2 - Q vs Random")
    player3Strategy = QStrategy()
    player3 = Player(constants.PLAYER_X_VAL, player3Strategy)
    board3 = Board()
    game3 = Game(player3, player2, board3)
    df = game3.playManyGames(10000)
    df.plot(x="Games", y=["X", "O", "Draws"], title="X - Q; O - Random")
    df.plot(x="Games", y=["X", "O", "Draws"])

    print("Game 3 - Random vs Q")
    player4Strategy = QStrategy()
    player4 = Player(constants.PLAYER_O_VAL, player4Strategy)
    board4 = Board()
    game4 = Game(player1, player4, board4)
    df = game4.playManyGames(10000)
    df.plot(x="Games", y=["X", "O", "Draws"], title="X - Random; O - Q")
    df.plot(x="Games", y=["X", "O", "Draws"])

    plt.show()







