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

#load our game font
custom_font = pygame.font.Font("assets/fonts/Brainfish_Rush.ttf", 128)

#define a function to draw background

def draw_background(surf):
    #load our tiles
    water = pygame.image.load("assets/sprites/water.png").convert()
    sand = pygame.image.load("assets/sprites/sand_top.png").convert()
    seagrass = pygame.image.load("assets/sprites/seagrass.png").convert()
    #use png transparency
    sand.set_colorkey((0,0,0))
    seagrass.set_colorkey((0,0,0))

    #fill the screen
    for x in range(0, screen_width, tile_size):
        for y in range(0, screen_height, tile_size):
            surf.blit(water, (x,y))

    #draw the sandy bottom
    for x in range(0, screen_width, tile_size):
        surf.blit(sand, (x, screen_height-tile_size))

    #add seagrass randomly at the bottom of the beach
    for _ in range(5):
        x = random.randint(0, screen_width)
        surf.blit(seagrass, (x, screen_height-tile_size*2))

    #draw the text
    text = custom_font.render("Chomp", True, (255, 0, 0))
    surf.blit(text, (screen_width/2 - text.get_width()/2, screen_height/2-text.get_height()/2))



def draw_fishes(surf):
    #load some fish tiles from sprites
    green_fish = pygame.image.load("assets/sprites/green_fish.png").convert()
    green_fish.set_colorkey((0,0,0)) #set png transparency

    for _ in range(5):
        x = random.randint(0, screen_width-tile_size)
        y = random.randint(0, screen_height-tile_size)
        surf.blit(green_fish, (x,y))

#Main Loop
running = True
background = screen.copy()
draw_background(background)
draw_fishes(background)

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