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


#adding the colliding sound
collision_sound = pygame.mixer.Sound("hurt.wav")
# Load and play the background music
pygame.mixer.music.load("background.wav")
pygame.mixer.music.play(-1)

# Main game function
def play_game(screen, clock, bullets_group, sea_mines_group):
    # Create a group to manage all sprites in the game
    all_sprites = pygame.sprite.Group()

    # Create and add the player fish to the sprite group
    player_fish = PlayerFish()
    all_sprites.add(player_fish)

    player_score = 0 #Initialize player_score before the loop
    player_lives = 3 #Initialize player_lives
    
    # Images for different fish types
    fish_images = ["fishes/orange_fish1.png", "fishes/green_fish.png", "fishes/yellow_fish.png"]

    # Generate initial fish objects and add them to the sprite group
    initial_fish_count = 15
    for _ in range(initial_fish_count):
        image_path = random.choice(fish_images)
        fish = Fishes(image_path, random.randint(1, 2))
        all_sprites.add(fish)

    # Timer variables for bullet and sea mine creation
    bullet_timer, bullet_frequency = 0, 500
    seamine_timer, seamine_frequency = 0, 1000

    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and player_lives <= 0:
                # Reset the game on mouse click if lives are zero
                player_lives = 3
                player_score = 0
                all_sprites.empty()
                bullets_group.empty()
                sea_mines_group.empty()

        # Update all sprites
        all_sprites.update()

        # Handle collisions between bullets and sea mines
        bullet_seamine_collisions = pygame.sprite.groupcollide(bullets_group, sea_mines_group, True, True)
        for seamine, bullets in bullet_seamine_collisions.items():
            for bullet in bullets:
                bullet.kill()
                seamine.kill()

        # Check collisions between player fish and other sprites
        collisions = pygame.sprite.spritecollide(player_fish, all_sprites, True)
        for collided_fish in collisions:
            if isinstance(collided_fish, Fishes):
                # Handle fish collisions
                player_score += collided_fish.value
                image_path = random.choice(fish_images)
                fish = Fishes(image_path, random.randint(1, 2))
                fish.rect.x = -fish.rect.width
                fish.rect.y = random.randint(0, HEIGHT - fish.rect.height)
                all_sprites.add(fish)
            elif isinstance(collided_fish, Seamine):
                # Handle seamine collisions
                player_lives -= 1
                if player_lives <= 0:
                    display_game_over(bullets_group, sea_mines_group)
                else:
                    collision_sound.play()

        # Check collisions between sea mines and fish bullets
        seamine_bullet_collisions = pygame.sprite.groupcollide(sea_mines_group, bullets_group, True, True)
        for seamine in seamine_bullet_collisions:
            seamine.kill()

        # Handle other sprite collisions (e.g., between fishes and bullets)
        hits = pygame.sprite.groupcollide(all_sprites, all_sprites, False, False)
        for hit in hits:
            for target in hits[hit]:
                if isinstance(hit, Fishes) and isinstance(target, Bullet):
                    player_score += hit.value
                    hit.kill()
                    target.kill()

        # Handle bullet shooting from the player fish
        bullet_timer += clock.get_rawtime()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and bullet_timer >= bullet_frequency:
            player_fish.shoot()
            bullet_timer = 0

        # Spawn sea mines at intervals
        seamine_timer += clock.get_rawtime()
        if seamine_timer >= seamine_frequency:
            seamine = Seamine()
            all_sprites.add(seamine)
            seamine_timer = 0

        # Draw everything on the screen
        screen.fill(WHITE)
        draw_background(screen)
        all_sprites.draw(screen)
        player_fish.draw(screen)
        player_fish.update()

        # Display player score and lives
        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {player_score} Lives: {player_lives}", True, BLACK)
        text_rect = text.get_rect()
        text_rect.topleft = (10, 10)
        screen.blit(text, text_rect)

        # Update display and maintain frame rate
        pygame.display.flip()
        clock.tick(60)




# Function to display the introduction screen
def display_intro():


    intro = True
    fish_sprites = pygame.sprite.Group() #create a sprite group for the fish

    for _ in range(20):
        image_path = random.choice(["fishes/orange_fish1.png", "fishes/green_fish.png", "fishes/yellow_fish.png"])
        fish = Fishes(image_path, random.randint(1,2))
        fish.rect.x = random.randint(0, WIDTH - fish.rect.width)
        fish.rect.y = random.randint(0, HEIGHT - fish.rect.height)
        fish_sprites.add(fish)

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                intro = False  # Exit the introduction loop on mouse click

        screen.fill(WHITE)
        draw_background(screen)

        #draw the fish sprites on the screen
        fish_sprites.draw(screen)

        #first text box
        font = pygame.font.Font(None, 48)
        text = font.render("Click anywhere to start", True, BLACK)
        text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        screen.blit(text, text_rect)

        #second text box
        font = pygame.font.Font(None, 20)
        additional_text = font.render("Objective: Eat as many fish a possible without running into the sea mines that will randomly appear.", True, BLACK)
        additional_text_rect = additional_text.get_rect(center=(WIDTH/2, HEIGHT/2 + 50))
        screen.blit(additional_text, additional_text_rect)

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


# putting the sound in
game_over_sound = pygame.mixer.Sound("game-over.wav")
# Display game over screen including high score
def display_game_over(bullets_group, sea_mines_group):
    global player_score
    game_over = True
    high_score = load_high_score()

    if player_score > high_score:
        high_score = player_score
        save_high_score(high_score)

    #play the game over sound
    game_over_sound.play()

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

        pygame.display.flip()
        clock.tick(60)

# Declare all_sprites as a global variable
all_sprites = pygame.sprite.Group()


# Main function
def main():
    global player_score, player_lives

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    #Display the introduction page
    display_intro()

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






