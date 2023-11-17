

import random

import pygame
import sys


#Initialize pygame
pygame.init()

#screen dimensions
screen_width = 800
screen_height = 600
tile_size = 64

#create screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('A beautiful beach in San Diego')

#define a function to draw background

def draw_background(surf):
    #load our tiles
    water = pygame.image.load("assets/sprites/water.png").convert()
    sand = pygame.image.load("assets/sprites/sand.png").convert()
    seamine = pygame.image.load("assets/sprites/seamine.png").convert()


    #use png transparency
    sand.set_colorkey((0,0,0))
    seamine.set_colorkey((254,254,254))


    #fill the screen
    for x in range(0, screen_width, tile_size):
        for y in range(0, screen_height, tile_size):
            surf.blit(water, (x,y))

    #draw the sandy bottom
    for x in range(0, screen_width, tile_size):
        surf.blit(sand, (x, screen_height-tile_size))

    #draw the mines randomly
    for _ in range(4):
        x = random.randint(0, screen_width - tile_size)
        y = random.randint(tile_size, screen_height - tile_size)
        i = random.randint(0, screen_width - tile_size)
        j = random.randint(tile_size, screen_height - tile_size)
        surf.blit(seamine, (x, y))
        surf.blit(seamine, (i, j))


    # load our game font
    custom_font = pygame.font.Font("assets/fonts/Brainfish_Rush.ttf", 70)

    #add the title "Fish are friends not food"
    text = custom_font.render("Fish are Friends Not Food", True, (255, 0, 0))
    surf.blit(text, (screen_width / 2 - text.get_width() / 2, screen_height / 2 - text.get_height() / 2))
    # how to get the tiles to not overlap each other



#Main Loop
running = True
background = screen.copy()
draw_background(background)

while running:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False
    #draw background
    screen.blit(background, (0,0))

    #update the display
    pygame.display.flip()

#quit pygame
pygame.quit()