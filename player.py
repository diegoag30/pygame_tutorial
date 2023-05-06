import os
from pickle import TRUE

import pygame

from support import import_folder


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0, 0)

        # player movement
        self.speed = 4
        self.gravity = 0.8
        self.jump_speed = -16  # Negativo para que sea hacia arriba

        # player status
        self.status = 'idle'
        self.is_facing_right = True
        self.on_ground = True
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False
        self.remaining_jump = 4

    def import_character_assets(self):
        character_path = os.path.join('assets', 'character', 'wind_hashashin', 'sprites')
        self.animations = {'idle': [], 'run': [], 'jump': [], 'fall': []}

        for animation in self.animations.keys():
            full_path = os.path.join(character_path, animation)
            self.animations[animation] = import_folder(full_path)

    def get_input(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a]:  # LEFT
            self.direction.x = -1
            self.is_facing_right = False
        elif keys_pressed[pygame.K_d]:  # RIGHT
            self.direction.x = 1
            self.is_facing_right = True
        else:
            self.direction.x = 0

        if keys_pressed[pygame.K_SPACE] and self.remaining_jump > 0:  # SPACE
            self.jump()
            # self.remaining_jump = self.remaining_jump - 1

    def get_status(self):
        if self.direction.y < 0:
            self.status = 'jump'
        elif self.direction.y > 1:
            self.status = 'fall'
        else:
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'idle'

    def jump(self):
        self.direction.y = self.jump_speed

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def animate(self):
        pass
        # animation = self.animations[self.status]

        # # Loop over the frame index
        # self.frame_index += self.animation_speed
        # if self.frame_index >= len(animation):
        #     self.frame_index = 0

        # image = animation[int(self.frame_index)]
        # if self.is_facing_right:
        #     self.image = image
        # else:
        #     flipped_image = pygame.transform.flip(image, True, False)
        #     self.image = flipped_image

        # # set the rectangle
        # if self.on_ground:
        #     self.rect = self.image.get_rect(midbottom=self.rect.midbottom)
        # elif self.on_ceiling:
        #     self.rect = self.image.get_rect(midtop=self.rect.midtop)
        # else:
        #     self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        self.get_input()
        self.get_status()
        self.animate()
