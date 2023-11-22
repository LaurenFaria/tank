import pygame
from game_parameters import *
import random
from fish import Fish, fishes
from enemy import Enemy,enemies

def draw_background(surf):
    #load our tiles
    water = pygame.image.load("../assets/sprites/water.png").convert()
    sand = pygame.image.load("../assets/sprites/sand.png").convert()
    seamine = pygame.image.load("../assets/sprites/seamine.png").convert()
    #use png transparency
    sand.set_colorkey((0,0,0))
    seamine.set_colorkey((255,255,255))

    #fill the screen
    for x in range(0, screen_width, tile_size):
        for y in range(0, screen_height, tile_size):
            surf.blit(water, (x,y))

    #draw the sandy bottom
    for x in range(0, screen_width, tile_size):
        surf.blit(sand, (x, screen_height-tile_size))

    #draw the mines randomy
    # draw the mines randomly
    for _ in range(4):
        x = random.randint(0, screen_width - tile_size)
        y = random.randint(tile_size, screen_height - tile_size)
        surf.blit(seamine, (x, y))

    #draw the text
    custom_font = pygame.font.Font("../assets/fonts/Brainfish_Rush.ttf", 48)
    text = custom_font.render("Chomp", True, (255, 0, 0))
    surf.blit(text, (screen_width/2 - text.get_width()/2, 0))

def add_fish(num_fish):
    for _ in range(num_fish):
        fishes.add(Fish(random.randint(screen_width, screen_width + 20),
                        random.randint(tile_size, screen_height - 2 * tile_size)))

def add_enemies(num_ememies):
    for _ in range(num_ememies):
        enemies.add(Enemy(random.randint(screen_width, screen_width +20),
                        random.randint(tile_size, screen_height - 2 * tile_size)))
