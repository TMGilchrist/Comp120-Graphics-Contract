import pygame


class sprite:

    image = 0

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
        sprite_base = pygame.Surface(self.size, pygame.SRCALPHA, 32)
        sprite_base.set_alpha(255)

        sprite_base.blit(self.base, (0, 0))
        sprite_base.blit(self.legs, (0, 0))
        sprite_base.blit(self.body, (0, 0))
        sprite_base.blit(self.head, (0, 0))
        sprite_base.blit(self.feet, (0, 0))

        # Save sprite
        self.image = sprite_base



    # Draw component images onto a base surface then save the surface as a single sprite
    def draw_with_position(self, base_pos, body_pos, legs_pos, head_pos):
        sprite_base = pygame.Surface(self.size, pygame.SRCALPHA, 32)
        sprite_base.set_alpha(255)

        sprite_base.blit(self.base, base_pos)
        sprite_base.blit(self.legs, legs_pos)
        sprite_base.blit(self.body, body_pos)
        sprite_base.blit(self.head, head_pos)
        sprite_base.blit(self.feet, (0, 0))

        # Save sprite
        self.image = sprite_base


    # Takes a list of properties (string) to update and a list of values (images) corresponding to each property
    def update(self, to_update, new_values):
        for i in range (0, len(to_update)):
            setattr(self, to_update[i], new_values[i])

        self.draw()



    # Save sprite with incrementing filename based on a .txt file of existing names
    def save_with_id(self, save_path, file_type):

        sprite_id = 0

        with open("spriteNames.txt", "a+") as f:
            for line in f:
                sprite_id += 1

            f.write("sprite" + str(sprite_id) + "\n")
            f.close()

        pygame.image.save(self.image, save_path + "/sprite" + str(sprite_id) + "." + file_type)
