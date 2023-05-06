from re import X

import pygame

from player import Player
from settings import WIDTH, tile_size
from tile import Tile


class Level():
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0  # Maneja el movimiento del mapa 0 estatico, 1> se mueva a la derecha

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_index, row in enumerate(layout):
            for col_index, col in enumerate(row):
                # Reemplaza la X con un Tile
                x = col_index * tile_size  # Coordenada X
                y = row_index * tile_size  # Coordenada Y
                if col == 'X':
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                # Reemplaza P con el player
                elif col == 'P':
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        # print(direction_x)
        if player_x < WIDTH * 0.1 and direction_x < 0:  # direction <0 es movimiento hacia la derecha
            self.world_shift = 8
            player.speed = 0
        elif player_x > WIDTH * 0.9 and direction_x > 0:  # direction <0 es movimiento hacia la izquierda
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 4

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True
                elif player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True

        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False

    def run(self):
        # Level Map
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)

        # Camera
        self.scroll_x()

        # player
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)
