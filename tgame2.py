import pygame
import sys
import random

from fish import Fish, fishes #importing a class and sprite group
#Initialize oygame
pygame.init()

#screen dimensions
screen_width = 800
screen_height = 600
tile_size = 64

#create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Getting the fish to move")

#load game font
custom_font = pygame.font.Font("assets/fonts/Brainfish_Rush.ttf" , 70)

#clock object
clock = pygame.time.Clock()

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


# Main loop
running = True
background = screen.copy()
draw_background(background)

#draw fish on the screen
for _ in range (5):
    fishes.add(Fish(random.randint(screen_width, screen_width*1.5), random.randint(tile_size, screen_height-2*tile_size)))
while running:
    for event in pygame.event.get():
        #print (event)
        if event.type == pygame.QUIT:
            running = False

    #check if any fish is off the screen
    for fish in fishes:
        if fish.rect.x < -fish.rect.width: #use the tile size
            fish.remove(fish) #remove the fish from the sprite group
            fishes.add(Fish(random.randint(screen_width, screen_width + 50), random.randint(tile_size, screen_height -2 *tile_size)))

    #draw the fish
    fishes.draw(screen)

    #update the display
    pygame.display.flip()

    #limit the frame rate
    clock.tick(60)

#quit pygame
pygame.quit()
sys.exit()


