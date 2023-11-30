import pygame
import random

# Constants
WIDTH, HEIGHT = 800, 600
tile_size = 64

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Initialize Pygame
pygame.init()

# Creating the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fish Are Friends, Not Food")
clock = pygame.time.Clock()

# Creating the font for the introduction
font = pygame.font.Font(None, 36)


def draw_background(surf):
    # Load our tiles from the assets folder
    sand = pygame.image.load("assets/sprites/sand.png").convert()
    water = pygame.image.load("assets/sprites/water.png").convert()
    seamine = pygame.image.load("assets/sprites/seamine.png").convert()
    # Make PNGs transparent
    sand.set_colorkey((0, 0, 0))
    seamine.set_colorkey((255, 255, 255))
    # Fill the screen with water
    for x in range(0, WIDTH, tile_size):
        for y in range(0, HEIGHT, tile_size):
            surf.blit(water, (x, y))
    # Draw a sandy bottom
    for x in range(0, WIDTH, tile_size):
        surf.blit(sand, (x, HEIGHT - tile_size))


class Fish(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        self.forward_image = pygame.image.load('fishes/red_fish.png').convert()
        self.forward_image.set_colorkey((255, 255, 255))
        self.reverse_image = pygame.transform.flip(self.forward_image, False, False)
        self.image = self.forward_image
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
        self.speed = random.uniform(1, 3)

    def update(self):
        self.rect.x += self.speed if self.direction == "right" else -self.speed

        if self.rect.right < 0:
            self.rect.left = WIDTH
        elif self.rect.left > WIDTH:
            self.rect.right = 0

        self.image = self.images[self.direction]


class Fishes(pygame.sprite.Sprite):
    def __init__(self, image_path, value):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
        self.velocity_x = random.uniform(0.5, 1.5)  # Horizontal velocity
        self.velocity_y = random.uniform(-0.5, 0.5)  # Vertical velocity
        self.value = value

    def update(self):
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y

        if self.rect.left > WIDTH:
            self.rect.right = 0
        elif self.rect.right < 0:
            self.rect.left = WIDTH
        if self.rect.top > HEIGHT:
            self.rect.bottom = 0
        elif self.rect.bottom < 0:
            self.rect.top = HEIGHT


class Seamine(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/sprites/seamine.png").convert_alpha()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))


def spawn_fish():
    fish_types = [
        ("fishes/orange_fish1.png", 5),
        ("fishes/green_fish.png", 5),
        ("fishes/yellow_fish.png", 5),
    ]
    for _ in range(10):
        image_path, value = random.choice(fish_types) #choses the fish randomly from the list
        fish = Fishes(image_path, value)
        all_sprites.add(fish) #add the fish sprites to the background

#add the seamines to the code
def spawn_seamines():
    for _ in range(5):
        seamine = Seamine()
        all_sprites.add(seamine)

#creating the intro page
def display_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #this will close the into page if anything is pressed
                pygame.quit()
                quit() #closse the first screen

            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                # Start the game when the button is clicked or any key is pressed
                intro = False #closes the event screen if any of the keys are pressed

        # Draw the introduction screen with background
        screen.fill(WHITE)
        draw_background(screen)
        text = font.render("Click anywhere or press any key to begin", True, BLACK)
        text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        screen.blit(text, text_rect)
        #fish_images = "fishes/green_fish.png"
        #fish_images_rect = fish_images.get_rect(center = (WIDTH/3, HEIGHT/3))
        #screen.blit(fish_images, fish_images_rect)


        pygame.display.flip()
        clock.tick(60)

#this brings up the game over page
def display_game_over():
    game_over = True
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Draw the game-over screen with the background
        screen.fill(WHITE)
        draw_background(screen)
        font = pygame.font.Font(None, 48)
        text = font.render("Game Over", True, BLACK)
        text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        screen.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(60)


# Game initialization
fish_value = 10
# Initialize player fish at the center of the screen
player_fish = Fish("fishes/red_fish.png")
player_fish.rect.center = (WIDTH // 2, HEIGHT // 2)  # Position at the center
all_sprites = pygame.sprite.Group()
all_sprites.add(player_fish)  # Add player fish to all_sprites group

spawn_fish()
spawn_seamines()

# Display introduction
display_intro()

# Inside the game loop
running = True
fish_deaths = 0  # Counter to track the number of times the player fish dies
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_fish.rect.x -= player_fish.speed
        player_fish.direction = "left"
        if player_fish.rect.left < 0:  # Boundary check
            player_fish.rect.left = 0

    if keys[pygame.K_RIGHT]:
        player_fish.rect.x += player_fish.speed
        player_fish.direction = "right"
        if player_fish.rect.right > WIDTH:  # Boundary check
            player_fish.rect.right = WIDTH

    if keys[pygame.K_UP]:
        player_fish.rect.y -= player_fish.speed
        player_fish.direction = "up"
        if player_fish.rect.top < 0:  # Boundary check
            player_fish.rect.top = 0

    if keys[pygame.K_DOWN]:
        player_fish.rect.y += player_fish.speed
        player_fish.direction = "down"
        if player_fish.rect.bottom > HEIGHT:  # Boundary check
            player_fish.rect.bottom = HEIGHT

    # Collision detection logic
    fish_collisions = pygame.sprite.spritecollide(player_fish, all_sprites, True)

    # Handling collisions
    for fish in fish_collisions:
        if isinstance(fish, Fishes):
            fish_value += fish.value
        elif isinstance(fish, Seamine) and fish != player_fish:
            fish_deaths += 1
            if fish_deaths >= 3:
                running = False  # Game over after 3 deaths

    # Clear the screen
    screen.fill(WHITE)

    # Draw the background
    draw_background(screen)

    # Render and display points at the top right corner
    font = pygame.font.Font(None, 36)
    text = font.render("Points: " + str(fish_value), True, BLACK)
    text_rect = text.get_rect()
    text_rect.topright = (WIDTH - 10, 10)
    screen.blit(text, text_rect)

    # Update all sprites
    all_sprites.update()

    # Draw all sprites
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

# Display game over screen
display_game_over()

pygame.quit()

