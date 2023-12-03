import pygame
import random

WIDTH, HEIGHT = 800, 600
tile_size = 64

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


