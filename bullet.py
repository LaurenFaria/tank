import pygame
from seamine import Seamine
WIDTH, HEIGHT = 800, 600

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 5))  # Adjust size as needed
        self.image.fill((255, 0, 0))  # Red bullet
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 8  # Adjust bullet speed as needed

    def update(self):
        self.rect.x += self.speed  # Move bullet horizontally
        if self.rect.x > WIDTH:  # If bullet goes off-screen, remove it
            self.kill()


