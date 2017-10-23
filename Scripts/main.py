import pygame
import glob
import random
from sprite import sprite

base = []
legs = []
body = []
head = []
feet = []

# Specify file type to load and the image directories
sprite_file_type = ".png"

path_to_assets = "D:/Uni/Programming/HereBeDragons/Assets"

# pathToAssets = "//tremictssan.fal.ac.uk\userdata\TG190896\My Documents\Py2.7\HereBeDragons\Assets"


# Might be better to use os.join for filepath
base_path = glob.glob(path_to_assets + "/Sprites/base/*" + sprite_file_type)
legs_path = glob.glob(path_to_assets + "/Sprites/legs/*" + sprite_file_type)
body_path = glob.glob(path_to_assets + "/Sprites/body/*" + sprite_file_type)
head_path = glob.glob(path_to_assets + "/Sprites/hair/*" + sprite_file_type)
feet_path = glob.glob(path_to_assets + "/Sprites/shoes/*" + sprite_file_type)

print("got paths")

# Adds all image files in path to lists
for filename in base_path:
    base.append(pygame.image.load(filename))

for filename in legs_path:
    legs.append(pygame.image.load(filename))

for filename in body_path:
    body.append(pygame.image.load(filename))

for filename in head_path:
    head.append(pygame.image.load(filename))

for filename in feet_path:
    feet.append(pygame.image.load(filename))

print("added sprites")

# Create new sprite with random component

# Arguments: Sprite Size (total canvas), baseImage bodyImage, headImage, feetImage, weaponImage
new_sprite = sprite((16, 16), random.choice(base), random.choice(legs), random.choice(body), random.choice(head), random.choice(feet), 0)

# Arguments: bodyPos, headPos, fileType
new_sprite.draw()
new_sprite.save_with_id(path_to_assets + "\Sprites\CustomSprites", "png")
