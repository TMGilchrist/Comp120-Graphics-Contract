import pygame


class sprite:

    # Initialise new sprite with component images
    def __init__(self, size, base, legs, body, head, feet, weapon):
        self.size = size
        self.base = base
        self.legs = legs
        self.body = body
        self.head = head
        self.feet = feet
        self.weapon = weapon



    # Draw component images onto a base surface then save the surface as a single sprite
    def draw(self):
        spriteBase = pygame.Surface(self.size, pygame.SRCALPHA, 32)
        spriteBase.set_alpha(255)

        spriteBase.blit(self.base, (0, 0))
        spriteBase.blit(self.legs, (0, 0))
        spriteBase.blit(self.body, (0, 0))
        spriteBase.blit(self.head, (0, 0))

        # Save sprite
        #self.saveWithID(spriteBase, "D:\Uni\Programming\HereBeDragons\Assets\Sprites\CustomSprites", fileType)
        #self.saveWithID(spriteBase, "//tremictssan.fal.ac.uk\userdata\TG190896\My Documents\Py2.7\HereBeDragons\Assets\Sprites\CustomSprites", fileType)

        return spriteBase



# Draw component images onto a base surface then save the surface as a single sprite
    def drawWithPosition(self, basePos, bodyPos, legsPos, headPos, fileType):
        spriteBase = pygame.Surface(self.size, pygame.SRCALPHA, 32)
        spriteBase.set_alpha(255)

        spriteBase.blit(self.base, basePos)
        spriteBase.blit(self.legs, legsPos)
        spriteBase.blit(self.body, bodyPos)
        spriteBase.blit(self.head, headPos)

        # Save sprite
        pygame.image.save(spriteBase, 'NewSprites/sprite.' + fileType)



# Save sprite with incrementing filename based on a .txt file of existing names
    def saveWithID(self, toSave, savePath, fileType):

        spriteID = 0

        with open("spriteNames.txt", "a+") as f:
            for line in f:
                spriteID += 1

            f.write("sprite" + str(spriteID) + "\n")
            f.close()

        pygame.image.save(toSave, savePath + "/sprite" + str(spriteID) + "." + fileType)
