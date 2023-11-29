import pygame
import random

WIDTH, HEIGHT = 800, 600
tile_size = 64

class Fish(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("fishes/red_fish.png").convert_alpha()
        self.image.set_colorkey((255, 255, 255))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
        self.speed = 3

    # Creating the player fish controls
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.image = pygame.transform.flip(self.image, True, False)
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.image = pygame.transform.flip(self.image, False, False)
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

