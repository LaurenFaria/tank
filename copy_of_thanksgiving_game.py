import pygame
import random
from fish import PlayerFish
from seamine import Seamine
from fishes import Fishes
from bullet import Bullet

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



# Main game function
def play_game(screen, clock, bullets_group, sea_mines_group):
    global player_score, player_lives, all_sprites

    all_sprites = pygame.sprite.Group()
    player_fish = PlayerFish()
    all_sprites.add(player_fish)
    fish_images = ["fishes/orange_fish1.png", "fishes/green_fish.png", "fishes/yellow_fish.png"]

    initial_fish_count = 15
    for _ in range(initial_fish_count):
        image_path = random.choice(["fishes/orange_fish1.png", "fishes/green_fish.png", "fishes/yellow_fish.png"])
        fish = Fishes(image_path, random.randint(1, 2))
        all_sprites.add(fish)

    bullet_timer = 0
    bullet_frequency = 500

    seamine_timer = 0
    seamine_frequency = 1000

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        all_sprites.update()

        bullet_seamine_collisions = pygame.sprite.groupcollide(bullets_group, sea_mines_group, True, False)

        for seamine, bullets in bullet_seamine_collisions.items():
            if len(bullets) >= 5:
                seamine.kill()

        collisions = pygame.sprite.spritecollide(player_fish, all_sprites, True)
        for collided_fish in collisions:
            if isinstance(collided_fish, Fishes):
                player_score += collided_fish.value
                # Add a new fish after collision
                image_path = random.choice(fish_images)
                fish = Fishes(image_path, random.randint(1,2))
                fish.rect.x = -fish.rect.width #off-screen on the left side
                fish.rect.y = random.randint(0, HEIGHT -fish.rect.height) #random Y position
                all_sprites.add(fish)
            elif isinstance(collided_fish, Seamine):
                player_lives -= 1
                if player_lives <= 0:
                    display_game_over()

        hits = pygame.sprite.groupcollide(all_sprites, all_sprites, False, False)
        for hit in hits:
            for target in hits[hit]:
                if isinstance(hit, Fishes) and isinstance(target, Bullet):
                    player_score += hit.value
                    hit.kill()
                    target.kill()

        bullet_timer += clock.get_rawtime()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and bullet_timer >= bullet_frequency:
            player_fish.shoot()
            bullet_timer = 0

        seamine_timer += clock.get_rawtime()
        if seamine_timer >= seamine_frequency:
            seamine = Seamine()
            all_sprites.add(seamine)
            seamine_timer = 0

        screen.fill(WHITE)
        draw_background(screen)
        all_sprites.draw(screen)
        player_fish.draw(screen)
        player_fish.update()

        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {player_score} Lives: {player_lives}", True, BLACK)
        text_rect = text.get_rect()
        text_rect.topleft = (10, 10)
        screen.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(60)


# Function to display the introduction screen
def display_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                intro = False  # Exit the introduction loop on mouse click

        screen.fill(WHITE)
        draw_background(screen)
        font = pygame.font.Font(None, 48)
        text = font.render("Click anywhere to start", True, BLACK)
        text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        screen.blit(text, text_rect)
        pygame.display.flip()
        clock.tick(60)

# ... (previous code remains unchanged)

# Function to save high score to a file
def save_high_score(score):
    with open("highscore.txt", "w") as file:
        file.write(str(score))

# Function to load high score from the file
def load_high_score():
    try:
        with open("highscore.txt", "r") as file:
            high_score = int(file.read())
    except FileNotFoundError:
        high_score = 0
    return high_score

# Display game over screen including high score
def display_game_over():
    global player_score
    game_over = True
    high_score = load_high_score()

    if player_score > high_score:
        high_score = player_score
        save_high_score(high_score)

    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(WHITE)
        draw_background(screen)
        font = pygame.font.Font(None, 36)
        text = font.render(f"Game Over - High Score: {high_score}", True, BLACK)
        text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 50))
        screen.blit(text, text_rect)

        font = pygame.font.Font(None, 24)
        restart_text = font.render("Click anywhere to restart", True, BLACK)
        restart_rect = restart_text.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 50))
        screen.blit(restart_text, restart_rect)

        pygame.display.flip()
        clock.tick(60)



# Main function
def main():
    global player_score, player_lives

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    # Create bullets_group and sea_mines_group
    bullets_group = pygame.sprite.Group()
    sea_mines_group = pygame.sprite.Group()

    player_score = 0
    player_lives = 3

    # Create initial sea mines and add them to sea_mines_group
    initial_seamine_count = 5
    for _ in range(initial_seamine_count):
        seamine = Seamine()
        all_sprites.add(seamine)
        sea_mines_group.add(seamine)

    # Pass these groups to play_game
    play_game(screen, clock, bullets_group, sea_mines_group)


if __name__ == "__main__":
    pygame.init()
    main()






class Laser(pygame.sprite.Sprite):
    speed = -11
    def __init__(self,x,y):
        self.image = pygame.image