import numpy as np
import pygame
from pygame.locals import *
from FieldGraphics import FieldGraphics
from NotFieldGraphics import NotFieldGraphics

WHITE = (255,255,255)
class Displayer:
    def __init__(self):
        pass
    def display(self, board):
        pygame.init()
        window = pygame.display.set_mode((490, 490))
        pygame.display.set_caption("Kolko i krzyzyk (work in progress)")
        spritesList = []
        for x in range(3):
            for y in range(3):
                spritesList.append(FieldGraphics(WHITE, 150, 150))
                spritesList[x*3+y].rect.x = 5+x*160
                spritesList[x*3+y].rect.y = 5+y*160
                spritesList[x*3+y].fieldNo = x*3+y
                isSign = False
                if board[x*3+y] == 1:
                    isSign = True
                    isCross = True
                elif board[9+x*3+y] == 1:
                    isSign = True
                    isCross = False
                if isSign:
                    spritesList[x*3+y].placeSign(isCross)

        fieldsSprites = pygame.sprite.Group(spritesList)
        gridSprite = NotFieldGraphics(WHITE, 490, 490)
        nonFieldsSprites = pygame.sprite.Group(gridSprite)
        fieldsSprites.update()
        nonFieldsSprites.update()
        window.fill(WHITE)
        fieldsSprites.draw(window)
        nonFieldsSprites.draw(window)
        pygame.display.flip()
        carryOn = True
        while carryOn:
            for event in pygame.event.get():
                 if event.type == QUIT:
                    carryOn = False
        return False
