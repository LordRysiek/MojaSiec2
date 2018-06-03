import numpy as np
from BoardTools import BoardTools
import random

class Tournament:
    def __init__(self, player1, player2):
        self.listOfMoveDatas = []
        self.player1 = player1
        self.player2 = player2
    def playGame(self, randomization1, randomization2):
        newGame = Game(self.player1, self.player2, randomization1, randomization2)
        while newGame.playOneMove():
            pass
        self.listOfMoveDatas.extend(newGame.listOfMoveDatas)
        return newGame.whoWon

class Game:
    def __init__(self, player1, player2, randomization1, randomization2):
        self.listOfMoveDatas = []
        self.whoWon = 0
        self.board = np.zeros((18,1))
        self.whoIsPlayingNow = 1
        self.tools = BoardTools()
        self.player1 = player1
        self.player2 = player2
        self.randomization1 = randomization1
        self.randomization2 = randomization2

    def playOneMove(self):
        move = np.zeros((9,1))
        if self.whoIsPlayingNow == 1:
            randomization = self.randomization1
            player = self.player1
        else:
            randomization = self.randomization2
            player = self.player2

        if random.random()<randomization:
            index = random.randint(0, 8)
            move[index, 0] = 1
            while(not self.tools.checkLegality(self.board, move)):
                move = np.zeros((9,1))
                index = random.randint(0, 8)
                move[index, 0] = 1
            self.listOfMoveDatas.append(MoveData(self.board, move))
        else:
            move[np.argmax(player.processVector(self.board*self.whoIsPlayingNow))]=1
            self.listOfMoveDatas.append(MoveData(self.board, move))
            if not self.tools.checkLegality(self.board, move):
                self.whoWon = -self.whoIsPlayingNow
                self.scoreMoves()
                return False

        self.tools.playMove(self.board, move)
        self.whoWon = self.tools.checkWinning(self.board)
        if self.whoWon != 0:
            self.scoreMoves()
            return False

        self.whoIsPlayingNow = -self.whoIsPlayingNow
        return True

    def scoreMoves(self):
        length = len(self.listOfMoveDatas)
        trigger = self.whoIsPlayingNow
        for i in range(length-1, -1, -1):
            self.listOfMoveDatas[i].points = trigger*self.whoWon
            trigger = -trigger


class MoveData:
    def __init__(self, board, move):
        self.board = board
        self.move = move
        self.points = 0
