import pygame
from sprite import sprite
import glob


class characterCreation:

    pathToAssets = "D:/Uni/Programming/HereBeDragons/Assets"
    # pathToAssets = "//tremictssan.fal.ac.uk\userdata\TG190896\My Documents\Py2.7\HereBeDragons\Assets"

    blankComponent = pygame.image.load(pathToAssets + "/Sprites/blankComponent.png")
    blankBase = pygame.image.load(pathToAssets + "/Sprites/base/base1.png")

    mainScreen = 0
    charScreen = 0

    playerChar = 0
    biggerCharImage = 0

    bodyChoices = []

    # Constuctor instantiates a sprite with a blank base
    def __init__(self, size, headList, bodyList):
        self.size = size
        #self.headList = headList
        self.bodyChoices = bodyList

        self.playerChar = self.loadBlankSprite()
        self.biggerCharImage = pygame.transform.scale(self.playerChar.image, (64, 64))


    # Draw the character creation window
    def drawWin(self):
        print("Drawing screen for first time")
        self.mainScreen = pygame.display.set_mode((self.size))

        self.charScreen = pygame.Surface(self.size)
        self.charScreen.fill((222, 184, 135))

        self.updateScreen()

        self.scrollComponents("body")

        # Keep window open until user closes it
        done = False

        while not done:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    done = True

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    done = True



    def updateScreen(self):
        # Update Screen
        self.biggerCharImage = pygame.transform.scale(self.playerChar.image, (64, 64))
        self.charScreen.blit(self.biggerCharImage, (400, 300))
        self.mainScreen.blit(self.charScreen, (0, 0))
        pygame.display.flip()

        print("Screen updated")

    # Method returns a sprite base
    def loadBlankSprite(self):
        # Create and draw a new sprite with a base image and blank components
        blankSprite = sprite((16, 16),self.blankBase , self.blankComponent, self.blankComponent, self.blankComponent, self.blankComponent, 0)
        blankSprite.draw()

        return blankSprite




    def scrollComponents(self, component):
        print("Scroll components running")
        fakeButton = 1
        index = -1

        while fakeButton != 2:
            fakeButton = int(raw_input("Input 1 for scroll forwards, -1 for scroll back"))

            if fakeButton == 1:
                index += 1

            elif fakeButton == -1:
                index -= 1

            else:
                break

            print("index = " + str(index))
            print("Updating sprite")

            self.playerChar.update([component], [getattr(self, component + "Choices")[index]])
            self.updateScreen()

        # return False



# Calling as test
bodies = []

for filename in glob.glob("D:/Uni/Programming/HereBeDragons/Assets/Sprites/body/*.png"):
    bodies.append(pygame.image.load(filename))

testWindow = characterCreation((800, 600), 0, bodies)
testWindow.drawWin()

#testWindow.scrollComponents("body")





