import pygame
import random
from fish import PlayerFish
from seamine import Seamine
from fishes import Fishes

# Constants
WIDTH, HEIGHT = 800, 600
tile_size = 64

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fish Are Friends, Not Food")
clock = pygame.time.Clock()

# Function to draw the background
def draw_background(surf):
    # Load tiles
    water = pygame.image.load("assets/sprites/water.png").convert()
    sand = pygame.image.load("assets/sprites/sand.png").convert()
    # Use PNG transparency
    sand.set_colorkey((0, 0, 0))

    # Fill the screen with water tiles
    for x in range(0, WIDTH, tile_size):
        for y in range(0, HEIGHT, tile_size):
            surf.blit(water, (x, y))

    # Draw the sandy bottom
    for x in range(0, WIDTH, tile_size):
        surf.blit(sand, (x, HEIGHT - tile_size))




all_sprites = pygame.sprite.Group()

# Creating the background fish and sea mines

# Main game function
def play_game():
    global player_score, player_lives

    player_fish = PlayerFish()
    player_fish.draw(screen)
    #all_sprites.add(player_fish)  # Add player fish to the sprite group

    # Create background fish (example)
    for _ in range(10):
        image_path = random.choice(["fishes/orange_fish1.png", "fishes/green_fish.png", "fishes/yellow_fish.png"])
        fish = Fishes(image_path, random.randint(1, 2))
        all_sprites.add(fish)

    # Create sea mines
    for _ in range(5):
        seamine = Seamine()
        all_sprites.add(seamine)



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Update player fish position based on arrow key presses
        all_sprites.update()

        # Collision detection
        collisions = pygame.sprite.spritecollide(player_fish, all_sprites, True)
        for collided_fish in collisions:
            if isinstance(collided_fish, Fishes):
                player_score += collided_fish.value
            elif isinstance(collided_fish, Seamine):
                player_lives -= 1
                if player_lives <= 0:
                    display_game_over()




        # Draw the game elements
        screen.fill(WHITE)
        draw_background(screen)
        all_sprites.draw(screen)  # Draw all sprites, including the player fish

        # Update the player's score and lives on the screen
        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {player_score} Lives: {player_lives}", True, BLACK)
        text_rect = text.get_rect()
        text_rect.topleft = (10, 10)
        screen.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(60)

# Display game over screen
def display_game_over():
    game_over = True
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(WHITE)
        draw_background(screen)
        font = pygame.font.Font(None, 48)
        text = font.render("Game Over", True, BLACK)
        text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        screen.blit(text, text_rect)
        pygame.display.flip()
        clock.tick(60)

# Main function
def main():
    global player_score, player_lives
    player_score = 0
    player_lives = 3

    play_game()

if __name__ == "__main__":
    main()

