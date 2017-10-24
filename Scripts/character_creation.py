import pygame
from sprite import sprite
import glob


class CharacterCreation:

    path_to_assets = "../Assets"

    blank_component = pygame.image.load(path_to_assets + "/Sprites/blankComponent.png")
    blank_base = pygame.image.load(path_to_assets + "/Sprites/base/base1.png")

    main_screen = 0
    char_screen = 0

    player_char = 0
    bigger_char_image = 0

    body_choices = []

    # Constuctor instantiates a sprite with a blank base
    def __init__(self, size, head_list, body_list):
        self.size = size
        #self.head_list = head_list
        self.body_choices = body_list

        self.player_char = self.load_blank_sprite()
        self.bigger_char_image = pygame.transform.scale(self.player_char.image, (64, 64))


    # Draw the character creation window
    def draw_win(self):
        print("Drawing screen for first time")
        self.main_screen = pygame.display.set_mode(self.size)

        self.char_screen = pygame.Surface(self.size)
        self.char_screen.fill((222, 184, 135))

        self.update_screen()

        self.scroll_components("body")

        # Keep window open until user closes it
        done = False

        while not done:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    done = True

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    done = True



    def update_screen(self):
        # Update Screen
        # self.bigger_char_image = pygame.transform.scale(self.player_char.image, (64, 64))
        self.char_screen.blit(self.player_char.image, (400, 300))
        self.main_screen.blit(self.char_screen, (0, 0))
        pygame.display.update()

        print("Screen updated")

    # Method returns a sprite base
    def load_blank_sprite(self):
        # Create and draw a new sprite with a base image and blank components
        blank_sprite = sprite((64, 64), pygame.transform.scale(self.blank_base, (64, 64)), self.blank_component, self.blank_component, self.blank_component, self.blank_component, 0)
        blank_sprite.draw()

        return blank_sprite




    def scroll_components(self, component):
        print("Scroll components running")
        fake_button = 1
        index = -1

        while True:
            for event in pygame.event.get():
                pass  # clear the event loop by doing nothing

            fake_button = int(raw_input("Input 1 for scroll forwards, -1 for scroll back"))

            if fake_button == 1:
                index += 1

            elif fake_button == -1:
                index -= 1

            else:
                break

            print("index = " + str(index))
            print("Updating sprite")

            self.player_char.update([component], [getattr(self, component + "_choices")[index]])
            self.update_screen()



# Calling as test
bodies = []

for filename in glob.glob("../Assets/Sprites/body/*.png"):
    bodies.append(pygame.transform.scale(pygame.image.load(filename), (64, 64)))
    # pygame.transform.scale(bodies[filename], (64, 64))

test_window = CharacterCreation((800, 600), 0, bodies)
test_window.draw_win()

#test_window.scroll_components("body")





