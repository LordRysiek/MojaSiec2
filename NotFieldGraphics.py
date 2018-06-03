from pygame.locals import *
import pygame

WHITE = (255,255,255)
GREY = (120,120,120)
class NotFieldGraphics(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.Surface([width, height])
       self.image.fill(color)
       self.image.set_colorkey(WHITE)
       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.image = pygame.image.load("grid.png").convert_alpha()
       self.rect = self.image.get_rect()
