import pygame
import math

mainScreen = pygame.display.set_mode((800, 600))

image = pygame.image.load('redPlanet.jpg').convert()


#Reduces a colour by a value (currently red by half)
def reduceColour(image, colour, decrease):

    print('reduceColour Function running')

    for x in range(image.get_width()):
        for y in range(image.get_height()):

            pixel = image.get_at((x, y))

            redVal = pixel.r
            greenVal = pixel.g
            blueVal = pixel.b

            redVal = redVal * 0.5
            image.set_at((x, y), (redVal, greenVal, blueVal))

    return


#Returns distance between two colours
def colourDistance(colour1, colour2):

    print('colourDistance function running')

    formula = (colour1.r - colour2.r)^2 + (colour1.g - colour2.g)^2 + (colour1.b - colour2.b)^2

    if formula <= 0:
        formula = formula * -1

    distance = math.sqrt(formula)

    return distance

#colour 1 = base colour, colour2 = colour being compared
def closeEnoughTo(colour1, colour2, tolerance):
    if (colourDistance(colour1, colour2) < tolerance):
        return True
    else:
        return False





def TurnColor():









red = pygame.Color(255, 0, 0)
crimson = pygame.Color(220, 20, 60)
blue = pygame.Color(0, 0 , 255)
green = pygame.Color(0, 255 , 0)


reduceColour(image, red, 10)

colourDistance(blue, red)

print(closeEnoughTo(red, crimson, 50))





# Update display
mainScreen.blit(image, (0,0))
pygame.display.flip()


# Keep window open until user closes it
done = False

while not done:
    for event in pygame.event.get():

        if event.type ==pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
