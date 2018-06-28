from Network import Network
from BoardTools import BoardTools
from Tournament import Tournament
from Displayer import Displayer
import numpy as np

#
from Network import Layer

playerRed = Network([18,2,3,9])



#print(playerRed.hiddenLayers[0].weights)
#print(playerRed.hiddenLayers[1].weights)
displayer = Displayer()
print("///////////Player red://///////////")
playerRed.displayText()
highlights=[]
database=[]
for j in range(10):
    tournament = Tournament(playerRed, playerRed)
    for i in range(1):
        tournament.playGame(0,0)
    database = database + tournament.listOfMoveDatas
    playerRed.learnFromGroupOfMoveDatas(database, 10)
    highlights=[mv.board for mv in tournament.listOfMoveDatas[0:10]]


print("///////////Player red://///////////")
playerRed.displayText()
tournament2 = Tournament(playerRed, playerRed)
for i in range(1):
    tournament2.playGame(0,0)

superBowl = highlights+[mv.board for mv in tournament2.listOfMoveDatas[0:10]]
displayer.displaySequence(superBowl)
 
