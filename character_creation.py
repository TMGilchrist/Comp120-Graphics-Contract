import pygame
from sprite import sprite


class displayCreationWin:


    pathToAssets = "//tremictssan.fal.ac.uk\userdata\TG190896\My Documents\Py2.7\HereBeDragons\Assets"
    blankComponent = pygame.image.load(pathToAssets + "/Sprites/blankComponent.png")
    blankBase = pygame.image.load(pathToAssets + "/Sprites/base/base1.png")


# Constuctor
    def __init__(self, size):
        self.size = size


# Draw the character creation window
    def drawWin(self):
        mainScreen = pygame.display.set_mode((self.size))

        charScreen = pygame.Surface(self.size)
        charScreen.fill((222, 184, 135))

        placeholder = self.loadBlankSprite()

        charScreen.blit(placeholder, (400, 300))


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



    def loadBlankSprite(self):

        playerChar = sprite((16, 16),self.blankBase , self.blankComponent, self.blankComponent, self.blankComponent, 0, 0)
        charImage = playerChar.draw()

        biggerCharImage = pygame.transform.scale(charImage, (64, 64))

        return biggerCharImage




testWindow = displayCreationWin((800, 600))
testWindow.drawWin()