import pygame

class sprite:

    #Initalise new sprite with component images
    def __init__(self, body, head, feet, weapon):
        self.body = body
        self.head = head
        self.feet = feet
        self.weapon = weapon


    #Draw component images onto a base surface then save the surface as a single sprite
    def draw(self, bodyPos, headPos, fileType):
        spriteBase = pygame.Surface((800, 600))

        spriteBase.blit(self.body, bodyPos)
        spriteBase.blit(self.head, headPos)

        # Save sprite
        pygame.image.save(spriteBase, 'sprite.' + fileType)
