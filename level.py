import pygame

from player.player import Player
from settings import TILE_SIZE, WIDTH
from tile import Tile


class Level():

    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0  # Maneja el movimiento del mapa 0 estatico, 1> se mueva a la derecha

    def setup_level(self, layout):
        """ Draws tiles and player on the screen in his respective coordinates bassed on a given level layout.
        Args:
            layout (Surface): Pygame surface where the tiles of the level will be drawn.
        """
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_index, row in enumerate(layout):
            for col_index, col in enumerate(row):
                # Gets the coordinates of the tile bassed on the index of the row and column
                x = col_index * TILE_SIZE  # Coordenada X
                y = row_index * TILE_SIZE  # Coordenada Y
                if col == 'X':
                    tile = Tile((x, y), TILE_SIZE)
                    self.tiles.add(tile)
                # Reemplaza P con el player
                elif col == 'P':
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)

    def scroll_x(self):
        """ Scrolls the level horizontally bassed on the player's position.
        """
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
        """
        Checks if the player collides with any tile in the level horizontally.
        """
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_movement_collision(self):
        """
        Checks if the player collides with any tile in the level vertically.
        """
        player = self.player.sprite
        player.apply_gravity()
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                player.getColissions(sprite)

        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False

    def player_jump(self, jump_flag):
        """ Sends a flag to the player to allow him to jump(when w is pressed one time not keep).
        """
        player = self.player.sprite
        player.allow_jump = jump_flag

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
