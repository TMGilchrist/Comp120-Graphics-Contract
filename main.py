import pygame

# Init display - only necessary when displaying in window
mainScreen = pygame.display.set_mode((800, 600))

spriteBase = pygame.Surface((800, 600))

# Load images to combine
pyImage1 = pygame.image.load('spritePlaceHolder1.jpeg')
pyImage2 = pygame.image.load('spritePlaceHolder2.jpeg')


'''
Add images to lists based on catgory (head, body, weapon, etc)
'''

'''
Choose one image from each list at random
'''

#Draw sprite components to the spriteBase surface to combine them into one
spriteBase.blit(pyImage1, (0, 0))
spriteBase.blit(pyImage2, (50, 0))


#Save sprite
pygame.image.save(spriteBase, 'sprite.jpg')


#Below code is only for displaying the changes in a pygame window. Unncessecary for program

# Update display
mainScreen.blit(spriteBase, (0,0))
pygame.display.flip()


# Keep window open until user closes it
done = False

while not done:
    for event in pygame.event.get():

        if event.type ==pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True


