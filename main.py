import pygame
import os

from sqlalchemy import true
from settings import *
from tile import Tile
from level import Level

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
BACKGROUND_COLOR = (0,0,0)
pygame.display.set_caption("Bienvenido al Juego")
level = Level(level_map,WIN)

FPS = 60
IMAGE_PATH = os.path.join('Assets','Hero Knight','Sprites','HeroKnight','Idle')
FIRST_IMAGE = os.path.join(IMAGE_PATH,'HeroKnight_Idle_0.png')
MAIN_CHARACTER = pygame.image.load(FIRST_IMAGE)
MAIN_CHARACTER_WIDHT, MAIN_CHARACTER_HEIGHT = 120,100
MAIN_CHARACTER = pygame.transform.scale(MAIN_CHARACTER, (MAIN_CHARACTER_WIDHT, MAIN_CHARACTER_HEIGHT))
VEL = 2
CHAR_STAND = [
    os.path.join(IMAGE_PATH,'HeroKnight_Idle_0.png'),
    os.path.join(IMAGE_PATH,'HeroKnight_Idle_1.png'),
    os.path.join(IMAGE_PATH,'HeroKnight_Idle_2.png'),
    os.path.join(IMAGE_PATH,'HeroKnight_Idle_3.png'),
    os.path.join(IMAGE_PATH,'HeroKnight_Idle_4.png'),
    os.path.join(IMAGE_PATH,'HeroKnight_Idle_5.png'),
    os.path.join(IMAGE_PATH,'HeroKnight_Idle_6.png'),
    os.path.join(IMAGE_PATH,'HeroKnight_Idle_7.png')
    ]

def draw_window():
    WIN.fill((BACKGROUND_COLOR))
    #WIN.blit(MAIN_CHARACTER,(player.x,player.y))
    pygame.display.update()
  

def main():
    is_jump = False
    jump_count = 10
    #player_one = pygame.Rect(20,400,MAIN_CHARACTER_WIDHT,MAIN_CHARACTER_HEIGHT)
    clock = pygame.time.Clock()
    run = True
    # MAIN LOOP
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        WIN.fill((BACKGROUND_COLOR))
        level.run()

        #draw_window()
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()