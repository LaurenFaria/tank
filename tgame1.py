import pygame
import sys
import random

#Initialize oygame
pygame.init()

#screen dimensions
screen_width = 800
screen_height = 600
tile_size = 64

#create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Putting the fish on the screen")

#load game font
custom_font = pygame.font.Font("assets/fonts/Brainfish_Rush.ttf" , 70)

def draw_background(surf):
    #Load our tiles from the assets folder
    sand = pygame.image.load("C:assets/sprites/sand.png").convert()
    water = pygame.image.load("assets/sprites/water.png").convert()
    seamine = pygame.image.load("assets/sprites/seamine.png").convert()
    #Make PNGs transparent
    sand.set_colorkey((0,0,0))
    seamine.set_colorkey((255, 255, 255))


    #fill the screen with water
    for x in range(0,screen_width,tile_size):
        for y in range(0, screen_height, tile_size):
            surf.blit(water, (x,y))

    #draw a sandy bottom
    for x in range (0, screen_width, tile_size):
        surf.blit(sand,(x,screen_height - tile_size))

    # draw the mines randomly
    for _ in range(4):
        x = random.randint(0, screen_width - tile_size)
        y = random.randint(tile_size, screen_height - tile_size)
        surf.blit(seamine, (x, y))

    #draw the text
    text = custom_font.render("Fish are firends not food", True, (255,29,0))
    #text = custom_font.render('Chomp', True, (255,29,0))
    surf.blit(text, (screen_width/2 - text.get_width()/2, screen_height/2 - 250))
def draw_fishes(surf):
    #Load our fish tiles onto our surface
    orange_fish =pygame.image.load('assets/sprites/orange_fish1.png')
    #set color key
    orange_fish.set_colorkey((255,255,255,))
    #load green fish
    green_fish = pygame.image.load('assets/sprites/green_fish.png')
    #flip fish
    green_fish = pygame.transform.flip(green_fish, False, False)
    # set color key for green fish
    green_fish.set_colorkey((255,255,255))
    green_fish=pygame.transform.flip(green_fish, True, False)
    #load the red fish onto our surface
    red_fish = pygame.image.load('assets/sprites/red_fish.png')
    red_fish.set_colorkey((255,255,255))
    #load the yellow fish to the screen
    yellow_fish = pygame.image.load('assets/sprites/yellow_fish.png')
    yellow_fish.set_colorkey((255,255,255))
    #flip the yellow fish
    yellow_fish= pygame.transform.flip(yellow_fish, True, False )

    #distribute our green fish on the screen randomly
    for _ in range(5):
        x = random.randint(0, screen_width-tile_size)
        y = random.randint(tile_size, screen_height-tile_size)
        i = random.randint(0, screen_width - tile_size)
        j = random.randint(tile_size, screen_height - tile_size)
        l = random.randint(0, screen_width-tile_size)
        k = random.randint(tile_size, screen_height - tile_size)
        a = random.randint(0, screen_width-tile_size)
        b = random.randint(tile_size, screen_height - tile_size)
        surf.blit(orange_fish, (x,y))
        surf.blit(green_fish,(i,j))
        surf.blit(red_fish,(l,k))
        surf.blit(yellow_fish,(a,b))


# Main loop
running = True
background = screen.copy()
draw_background(background)
draw_fishes(background)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the background
    screen.blit(background, (0, 0))

    # update the display
    pygame.display.flip()

pygame.quit()