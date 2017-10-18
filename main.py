import pygame
import glob
import random
from sprite import sprite


body = []
head = []

#Specify file type to load and the image directories
spriteFileType = "jpeg"
bodyPath = glob.glob("SpriteComponents/body/*" + spriteFileType)
headPath = glob.glob("SpriteComponents/head/*" + spriteFileType)

#Adds all image files in path to lists
for filename in bodyPath:
    body.append(pygame.image.load(filename))

for filename in headPath:
    head.append(pygame.image.load(filename))



# Create new sprite with random component

# Arguments: Sprite Size (total canvas), bodyImage, headImage, feetImage, weaponImage
newSprite = sprite((100, 100), random.choice(body), random.choice(head), 0, 0)

# Arguments: bodyPos, headPos, fileType
newSprite.draw((40, 40), (60, 40), 'png')
