import pygame
import glob
import random
from sprite import sprite

base = []
legs = []
body = []
head = []

# Specify file type to load and the image directories
spriteFileType = ".png"

# pathToAssets = "D:/Uni/Programming/HereBeDragons/Assets"

pathToAssets = "//tremictssan.fal.ac.uk\userdata\TG190896\My Documents\Py2.7\HereBeDragons\Assets"


basePath = glob.glob(pathToAssets + "/Sprites/base/*" + spriteFileType)
legsPath = glob.glob(pathToAssets + "/Sprites/legs/*" + spriteFileType)
bodyPath = glob.glob(pathToAssets + "/Sprites/body/*" + spriteFileType)
headPath = glob.glob(pathToAssets + "/Sprites/hair/*" + spriteFileType)

print("got paths")

# Adds all image files in path to lists
for filename in basePath:
    base.append(pygame.image.load(filename))

for filename in legsPath:
    legs.append(pygame.image.load(filename))

for filename in bodyPath:
    body.append(pygame.image.load(filename))

for filename in headPath:
    head.append(pygame.image.load(filename))

print("added sprites")

# Create new sprite with random component

# Arguments: Sprite Size (total canvas), baseImage bodyImage, headImage, feetImage, weaponImage
newSprite = sprite((16, 16), random.choice(base), random.choice(legs), random.choice(body), random.choice(head), 0, 0)

# Arguments: bodyPos, headPos, fileType
newSprite.draw()
newSprite.saveWithID(pathToAssets + "\Sprites\CustomSprites", "png")
