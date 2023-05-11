import os

import pygame

from level import Level
from settings import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND_COLOR = (0, 0, 0)
pygame.display.set_caption("Bienvenido al Juego")
level = Level(level_map, WIN)

FPS = 60
IMAGE_PATH = os.path.join('assets', 'character', 'wind_hashashin', 'sprites', 'idle')
FIRST_IMAGE = os.path.join(IMAGE_PATH, 'idle_1.png')
MAIN_CHARACTER = pygame.image.load(FIRST_IMAGE)
MAIN_CHARACTER_WIDHT, MAIN_CHARACTER_HEIGHT = 120, 100
MAIN_CHARACTER = pygame.transform.scale(MAIN_CHARACTER, (MAIN_CHARACTER_WIDHT, MAIN_CHARACTER_HEIGHT))
VEL = 2
CHAR_STAND = [
    os.path.join(IMAGE_PATH, 'idle_1.png'),
    os.path.join(IMAGE_PATH, 'idle_2.png'),
    os.path.join(IMAGE_PATH, 'idle_3.png'),
    os.path.join(IMAGE_PATH, 'idle_4.png'),
    os.path.join(IMAGE_PATH, 'idle_5.png'),
    os.path.join(IMAGE_PATH, 'idle_6.png'),
    os.path.join(IMAGE_PATH, 'idle_7.png'),
    os.path.join(IMAGE_PATH, 'idle_8.png')
]


def draw_window():
    WIN.fill((BACKGROUND_COLOR))
    # WIN.blit(MAIN_CHARACTER,(player.x,player.y))
    pygame.display.update()


def main():
    # player_one = pygame.Rect(20,400,MAIN_CHARACTER_WIDHT,MAIN_CHARACTER_HEIGHT)
    clock = pygame.time.Clock()
    run = True
    # MAIN LOOP
    jump_count = 0
    jump_flag = False
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    jump_flag = True
                    level.player_jump(jump_flag)

                   # print("Tecla apretada " + str(jump_count) + " veces")

        WIN.fill((BACKGROUND_COLOR))
        level.run()

        # draw_window()
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
