import pygame


class sprite:

    # Initialise new sprite with component images
    def __init__(self, size, body, head, feet, weapon):
        self.body = body
        self.head = head
        self.feet = feet
        self.weapon = weapon
        self.size = size


# Draw component images onto a base surface then save the surface as a single sprite
    def draw(self, bodyPos, headPos, fileType):
        spriteBase = pygame.Surface(self.size, pygame.SRCALPHA, 32)

        spriteBase.set_alpha(255)

        spriteBase.blit(self.body, bodyPos)
        spriteBase.blit(self.head, headPos)

        # Save sprite
        pygame.image.save(spriteBase, 'NewSprites/sprite.' + fileType)