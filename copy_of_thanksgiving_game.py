import pygame
import random

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



# Creating the player fish
class Fishes(pygame.sprite.Sprite):
    def __init__(self, image_path, value):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
        self.velocity = random.uniform(1, 3)
        self.value = value  # Assign specific values to each type of fish


class PlayerFish(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("fishes/red_fish.png").convert_alpha()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed = 5

    def draw(self, surf):
        surf.blit(self.image, self.rect)


    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Ensure the player fish stays within the game window
        self.rect.x = max(0, min(self.rect.x, WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, HEIGHT - self.rect.height))

all_sprites = pygame.sprite.Group()

# Creating the background fish and sea mines
class Fishes(pygame.sprite.Sprite):
    def __init__(self, image_path, value):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.image.set_colorkey((255,255,255))
        self.rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
        self.velocity = random.uniform(1, 3)
        self.value = value  # Assign specific values to each type of fish

        # Inside the play_game() function where fish objects are created:
        # Create background fish (example)
    fish_values = {
        "fishes/orange_fish1.png": 5,
        "fishes/green_fish.png": 3,
        "fishes/yellow_fish.png": 4,
        }
    for _ in range(10):
        image_path = random.choice(list(fish_values.keys()))
        fish = Fishes(image_path, fish_values[image_path])
        all_sprites.add(fish)

    def update(self):
        self.rect.x += self.velocity
        if self.rect.left > WIDTH:
            self.rect.right = 0


#define the seamine class
class Seamine(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/sprites/seamine.png").convert_alpha()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))

    # Update method to keep the sea mines stationary
    def update(self):
        pass  # No update logic for the sea mines; they remain stationary

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

