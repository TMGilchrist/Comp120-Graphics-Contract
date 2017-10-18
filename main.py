import pygame
from sprite import sprite

#Load images for sprite components. Images should be loaded into lists or arrays for each component
body = pygame.image.load('spritePlaceHolder1.jpeg')
head = pygame.image.load('spritePlaceHolder2.jpeg')

#Create new sprite with selected components. Components should be taken randomly from list
newSprite = sprite(body, head, 0, 0)
newSprite.draw((0, 0), (0, 0), 'jpg')
