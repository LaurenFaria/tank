import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooting Game")
clock = pygame.time.Clock()

# Player object
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 10
player_speed = 5

# Pellet object
pellet_width = 5
pellet_height = 15
pellet_color = RED
pellet_speed = 7
pellets = []

# Enemy object
enemy_size = 50
enemy_speed = 3
enemies = []

# Create multiple enemies
for _ in range(5):
    enemies.append(pygame.Rect(random.randint(0, WIDTH - enemy_size), random.randint(50, 200), enemy_size, enemy_size))

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    # Move and draw enemies
    for enemy in enemies[:]:
        pygame.draw.rect(screen, RED, enemy)
        enemy.y += enemy_speed
        if enemy.y > HEIGHT:
            enemy.y = random.randint(-200, -50)
            enemy.x = random.randint(0, WIDTH - enemy_size)

    # Check collision between pellets and enemies
    for enemy in enemies[:]:
        for pellet in pellets[:]:
            if enemy.colliderect(pellet):
                pellets.remove(pellet)
                enemies.remove(enemy)
                break

    # Move and draw pellets
    for pellet in pellets[:]:
        pellet.y -= pellet_speed
        pygame.draw.rect(screen, pellet_color, pellet)
        if pellet.y < 0:
            pellets.remove(pellet)

    # Draw player
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))

    # Shooting mechanism
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        pellets.append(pygame.Rect(player_x + player_size // 2 - pellet_width // 2, player_y, pellet_width, pellet_height))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()

