import pygame
import sys
from game_parameters import *
from player import Player
from background import draw_background, add_fish, add_enemies
from enemy import Enemy, enemies
from fish import Fish, fishes

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("a school of moving fish")

# Clock object
clock = pygame.time.Clock()

# Main loop
running = True
background = screen.copy()
draw_background(background)

# Draw fish on screen
add_fish(5)

# Add enemy to the screen
add_enemies(3)

# Draw player fish
player = Player(screen_width/2, screen_height/2)

# Draw enemy fish
enemy = Enemy(screen_width/2, screen_height/2)

# Load new font to keep score
score = 0
score_font = pygame.font.Font("../assets/fonts/Brainfish_Rush.ttf", 48)

# Load new sound
#chomp = pygame.mixer.Sound("../assets/sounds/chomp.wav")
#pardon_me = pygame.mixer.Sound("../assets/sounds/Movie-08.wav")
#hurt = pygame.mixer.Sound("../assets/sounds/hurt.wav")
#bubbles = pygame.mixer.Sound("../assets/sounds/bubbles.wav")

# Add alternate and game over
life_icon = pygame.image.load("../assets/sprites/orange_fish1.png").convert()
life_icon.set_colorkey((0, 0, 0))

# Set the number of lives
lives = NUM_LIVES

while lives > 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Control our player fish with arrow keys
        player.stop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # Play chomp sound
                #pygame.mixer.Sound.play(pardon_me)
                player.move_up()
            if event.key == pygame.K_DOWN:
                player.move_down()
            if event.key == pygame.K_LEFT:
                player.move_left()
            if event.key == pygame.K_RIGHT:
                player.move_right()

    # Draw background
    screen.blit(background, (0, 0))

    # Update player fish
    player.update()

    # Check for collisions between the player and fish - use group collision method
    result = pygame.sprite.spritecollide(player, fishes, True)
    if result:
        # Play chomp sound
        #pygame.mixer.Sound.play(chomp)
        score += len(result)
        add_fish(len(result))

    fishes.update()

    # Check if player collides with enemy fish
    result = pygame.sprite.spritecollide(player, enemies, True)
    if result:
        # Play hurt sound
        #pygame.mixer.Sound.play(hurt)
        lives -= len(result)
        add_enemies(len(result))

    # Check if fish have left the screen
    for fish in fishes:
        if fish.rect.x < -fish.rect.width:
            fishes.remove(fish)
            add_fish(1)

    # Check if any enemy is off the screen
    for enemy in enemies:
        if enemy.rect.x < -enemy.rect.width:
            enemies.remove(enemy)
            add_enemies(1)

    # Draw the fish
    fishes.draw(screen)

    # Draw the player fish
    player.draw(screen)

    # Draw enemy fish
    enemies.update()

    # Update score font
    text = score_font.render(f"{score}", True, (255, 0, 0))
    screen.blit(text, (screen_width - text.get_width() / 2 - 30, 0))

    # Draw lives in the lower left corner
    for i in range(lives):
        screen.blit(life_icon, (i * tile_size, screen_height - tile_size))

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Create a new background when the game is over
screen.blit(background, (0, 0))

# Show game over message
message = score_font.render('GAME OVER ', True, (0, 0, 0))
screen.blit(message, (screen_width/2 - message.get_width() / 2, screen_height/2))

# Show final score
score_text = score_font.render(f"SCORE: {score}", True, (0, 0, 0))
screen.blit(score_text, (screen_width/2 - score_text.get_width()/2, screen_height/2 + score_text.get_height()))

# Update the display
pygame.display.flip()

# Play game over sound effect
#pygame.mixer.Sound.play(bubbles)

# Wait for the user to exit the game
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Limit the frame rate
    clock.tick(60)

pygame.quit()

