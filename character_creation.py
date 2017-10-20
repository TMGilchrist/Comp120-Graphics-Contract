import pygame
from sprite import sprite


class displayCreationWin:


    pathToAssets = "//tremictssan.fal.ac.uk\userdata\TG190896\My Documents\Py2.7\HereBeDragons\Assets"
    blankComponent = pygame.image.load(pathToAssets + "/Sprites/blankComponent.png")
    blankBase = pygame.image.load(pathToAssets + "/Sprites/base/base1.png")

    playerChar = 0

    # Constuctor
    def __init__(self, size):
        self.size = size
        self.playerChar = self.loadBlankSprite()



    # Draw the character creation window
    def drawWin(self):
        mainScreen = pygame.display.set_mode((self.size))

        charScreen = pygame.Surface(self.size)
        charScreen.fill((222, 184, 135))



        self.playerChar.update(["legs", "body"], [self.pathToAssets + "/Sprites/legs/legs0.png", self.pathToAssets + "/Sprites/body/bodies0.png" ])
        biggerCharImage = pygame.transform.scale(self.playerChar.image, (64, 64))

        charScreen.blit(biggerCharImage, (400, 300))



        # Update Screen
        mainScreen.blit(charScreen, (0, 0))
        pygame.display.flip()


        # Keep window open until user closes it
        done = False

        while not done:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    done = True

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    done = True




    # Method returns a sprite base
    def loadBlankSprite(self):
        # Create and draw a new sprite with a base image and blank components
        blankSprite = sprite((16, 16),self.blankBase , self.blankComponent, self.blankComponent, self.blankComponent, 0, 0)
        blankSprite.draw()

        return blankSprite



    # def drawSpriteComponent(self, spriteToUpdate, component):




# Calling as test
testWindow = displayCreationWin((800, 600))
testWindow.drawWin()