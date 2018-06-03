import numpy as np
import pygame
from pygame.locals import *
from FieldGraphics import FieldGraphics
from NotFieldGraphics import NotFieldGraphics
from BoardTools import BoardTools

WHITE = (255,255,255)
GREY = (120,120,120)
board = np.zeros((18,1), dtype=int)
boardTools = BoardTools()
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


fieldsSprites = pygame.sprite.Group(spritesList)
gridSprite = NotFieldGraphics(WHITE, 490, 490)
nonFieldsSprites = pygame.sprite.Group(gridSprite)

carryOn = True
isCross = True
clock=pygame.time.Clock()
while carryOn:
    for event in pygame.event.get():
         if event.type == QUIT:
            carryOn = False
         elif event.type == pygame.MOUSEBUTTONUP:
             pos = pygame.mouse.get_pos()
             clicked_sprites = [s for s in fieldsSprites if s.rect.collidepoint(pos)]
             for sprite in clicked_sprites:
                 print("U clickin' on sprite, pal")
                 sprite.placeSign(isCross)
                 if isCross:
                     board[sprite.fieldNo] = 1
                 else:
                     board[9+sprite.fieldNo] = 1
                 isCross = not isCross
    fieldsSprites.update()
    nonFieldsSprites.update()
    window.fill(WHITE)
    fieldsSprites.draw(window)
    nonFieldsSprites.draw(window)
    #Refresh Screen
    pygame.display.flip()
    clock.tick(60)
    if boardTools.checkWinning(board):
        carryOn = False
pygame.quit()
