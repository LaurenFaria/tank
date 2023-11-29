import pygame
import random
import os
pygame.init()
# Constants
WIDTH, HEIGHT = 800, 600
tile_size = 64
# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
# Creating the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fish are friends not food")
clock = pygame.time.Clock()
# Creating the font for the introduction
font = pygame.font.Font(None, 36)
text = font.render("Click anywhere to begin", True, RED)
text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
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
# Creating the player fish
class Fish(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
        self.speed = 3
    # Creating the player fish controls
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
class Fishes(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
        self.velocity = random.uniform(1, 3)  # Random initial velocity
    def update(self):
        self.rect.x += self.velocity
        if self.rect.left > WIDTH:
            self.rect.right = 0  # Reset the fish when it goes off the screen
# Create the fish
fish = Fish("fishes/red_fish.png")
all_sprites = pygame.sprite.Group()
all_sprites.add(fish)
# Create different kinds of fish (adjust the number based on your preference)

fish_images = [
    "fishes/orange_fish1.png",
    "fishes/green_fish.png",
    "fishes/yellow_fish.png",
]

for image in fish_images:
    fish = Fishes(image)
    all_sprites.add(fish)
    all_sprites.add(fish)
# Creating the seamines
class Seamine(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/sprites/seamine.png").convert_alpha()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
# Create the seamines
seamine_count = 5
all_seamines = pygame.sprite.Group()
for _ in range(seamine_count):
    seamine = Seamine()
    all_sprites.add(seamine)
    all_seamines.add(seamine)
# Game after the introduction

fish_value = 0
required_value = 100
fish_lives = 3
intro_done = False
running = True
while running and not intro_done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            intro_done = True
    screen.fill(WHITE)

    # Draw the background on the introduction page
    draw_background(screen)
    screen.blit(text, text_rect)
    pygame.display.flip()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Draw the background
    draw_background(screen)
    all_sprites.update()
    # Check for collisions with fish
    hits = pygame.sprite.spritecollide(fish, all_sprites, True)
    for hit in hits:
        if isinstance(hit, Fishes):
            fish_value += 10
    if fish_value >= required_value:
        all_sprites.empty()
        new_fish = Fishes("fishes/yellow_fish.png")
        all_sprites.add(new_fish)
        all_sprites.add(new_fish)
        fish_value = 0
    collisions = pygame.sprite.spritecollide(fish, all_seamines, False)
    if collisions:
        fish_lives -= 1
        fish.rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
    if fish_lives <= 0:
        running = False
    # Draw the sprites
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()