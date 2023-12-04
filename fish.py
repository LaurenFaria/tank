import pygame
import random
from bullet import Bullet

# Constants
WIDTH, HEIGHT = 800, 600

class PlayerFish(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Load the fish image and set its initial properties
        self.image = pygame.image.load("fishes/red_fish.png").convert_alpha()
        self.image.set_colorkey((255, 255, 255))
        self.original_image = self.image.copy()  # Create a copy to maintain the original for flipping
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)  # Initial position
        self.speed = 5  # Movement speed
        self.bullet_speed = 8  # Bullet speed
        self.bullets = pygame.sprite.Group()  # Group to manage bullets
        self.direction = "left"  # Initially facing left
        self.base_size = self.rect.size #base size of the fish


        self.size_multiplier = 1 #size multipluer based on the score

    def update(self, player_score = 0):
        # Update the size of the fish based on the size multiplier and player's score
        self.size_multiplier = 1.0 + (player_score / 100)  # Adjust this ratio as needed
        new_width = int(self.original_image.get_width() * self.size_multiplier)
        new_height = int(self.original_image.get_height() * self.size_multiplier)
        self.image = pygame.transform.scale(self.original_image, (new_width, new_height))
        self.rect = self.image.get_rect(center=self.rect.center)

        # Get the pressed keys
        keys = pygame.key.get_pressed()



        # Move the fish left, right, up, and down
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.direction = "left"  # Set direction to left when moving left
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.direction = "right"  # Set direction to right when moving right
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed  # Move up
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed  # Move down

        self.bullets.update()  # Update bullets

        # Ensure the player fish stays within the game window
        self.rect.x = max(0, min(self.rect.x, WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, HEIGHT - self.rect.height))

        if keys[pygame.K_SPACE]:
            self.shoot()  # Shoot bullets when space is pressed

    def draw(self, surface):
        # Draw the fish and bullets on the screen
        if self.direction == "left":
            surface.blit(self.image, self.rect)  # Draw the fish facing left
        else:
            # Flip the fish image horizontally when moving right
            flipped_image = pygame.transform.flip(self.image, True, False)
            surface.blit(flipped_image, self.rect)

        self.bullets.draw(surface)  # Draw bullets

    def shoot(self):
        bullet = Bullet(self.rect.right, self.rect.centery)  # Create a bullet
        self.bullets.add(bullet)  # Add bullet to bullets group

