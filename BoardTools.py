import numpy as np
import math

class BoardTools:
        def checkWinning(self, originalBoard):
            myBoard, opponentsBoard = self.vectorToBoards(originalBoard)
            rowLength = myBoard.shape[0]
            ones = np.ones(rowLength,)

            for row in range(rowLength):
                if np.array_equal(myBoard[:, row],ones):
                    return 1
                elif np.array_equal(opponentsBoard[:, row],ones):
                    return -1

            for column in range(rowLength):
                if np.array_equal(myBoard[column, :],ones):
                    return 1
                elif np.array_equal(opponentsBoard[column, :],ones):
                    return -1

            if np.array_equal(np.diag(myBoard),ones):
                return 1
            elif np.array_equal(np.diag(opponentsBoard),ones):
                return -1
            newMyBoard = np.fliplr(myBoard)
            newOpponentsBoard = np.fliplr(opponentsBoard)
            if np.array_equal(np.diag(newMyBoard),ones):
                return 1
            elif np.array_equal(np.diag(newOpponentsBoard),ones):
                return -1

            return 0

        def vectorToBoards(self, board):
            length = math.ceil(board.shape[0]/2)
            myBoard = board[0:length, 0]
            opponentsBoard = board[length:length*2,0]
            size = math.ceil(math.sqrt(myBoard.shape[0]))
            return np.reshape(myBoard, (size, size)), np.reshape(opponentsBoard, (size, size))

        def checkLegality(self, board, move):
            for i in range(move.shape[0]):
                if move[i,0]==1 and (board[i,0]!=0 or board[9+i,0]!=0):
                    return False
            return True

        def playMove(self, board, move):
            for i in range(len(move)):
                if move[i] == 1:
                    board[i] = 1
                    return
                elif move[i] == -1:
                    board[9+i] = 1
                    return
