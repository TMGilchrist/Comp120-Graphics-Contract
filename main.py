import pygame

# Init display
mainScreen = pygame.display.set_mode((800, 600))

# Load images to combine
pyImage1 = pygame.image.load('redSquareSprite.png')
pyImage2 = pygame.image.load('smallBlue.png')


'''
Add images to lists based on catgory (head, body, weapon, etc)
'''




# Clone base image then merge secondary image onto it
merged = pyImage1.copy()
merged.blit(pyImage2, (0, 0))

pygame.image.save(merged, 'mergedShape.jpg')


# Update display
mainScreen.blit(merged, (0,0))
pygame.display.flip()


# Keep window open until user closes it
done = False

while not done:
    for event in pygame.event.get():

        if event.type ==pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
