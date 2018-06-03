from Network import Network
from BoardTools import BoardTools
from Tournament import Tournament
from Displayer import Displayer
import numpy as np


playerRed = Network([18,50,9])
playerBlue = Network([18,30,9])

#print(playerRed.hiddenLayers[0].weights)
#print(playerRed.hiddenLayers[1].weights)
displayer = Displayer()
tournament = Tournament(playerRed, playerBlue)
tournament.playGame(0.1,0.1)

"""tools = BoardTools()
board = np.zeros((18,1))
move = [0,0,0,0,0,0,0,1,0]
tools.playMove(board, move)
move = [0,0,0,0,-1,0,0,0,0]
tools.playMove(board, move)
move = [0,1,0,0,0,0,0,0,0]
tools.playMove(board, move)
print(board)
displayer.display(board)"""
displayer.display(tournament.listOfMoveDatas[2].board)
