import pygame
import random
from bullet import Bullet

# Constants
WIDTH, HEIGHT = 800, 600

class PlayerFish(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("fishes/red_fish.png").convert_alpha()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed = 5
        self.bullet_speed = 8
        self.bullets = pygame.sprite.Group()

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

        self.bullets.update()

        # Ensure the player fish stays within the game window
        self.rect.x = max(0, min(self.rect.x, WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, HEIGHT - self.rect.height))

        if keys[pygame.K_SPACE]:
            self.shoot()

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        self.bullets.draw(surface)

    def shoot(self):
        bullet = Bullet(self.rect.right, self.rect.centery)  # Adjust position of the bullet
        self.bullets.add(bullet)  # Add bullet to bullets group
