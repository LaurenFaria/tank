# create a pygame sprite class for a fish
import os
import random
import pygame

# create a pygame sprite class for a fish
import random
import pygame

MIN_SPEED = 0.5
MAX_SPEED = 3

class Fish(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(f"../fishes/red_fish.png").convert()
        #self.image2 = pygame.image.load(f"../fishes/yellow_fish.png").convert()
        #self.image3 = pygame.image.load(f"../fishes/orange_fish1.png").convert()
        #self.image4 = pygame.image.load("f../fishes/green_fish.png").convert()
        self.image.set_colorkey((255,255,255))
        #self.image2.set_colorkey((255, 255, 255))
        #self.image3.set_colorkey((255,255,255))
        #self.image4.set_colorkey((255,255,255))
        #self.image.set_colorkey((255,255,255))
        self.image = pygame.transform.flip(self.image2, False, False)
        self.rect = self.image.get_rect()  # Corrected from self.rect - self.image.get_rect()
        #self.rect = self.image2.get_rect()
        self.x = x
        self.y = y
        self.speed = random.uniform(MIN_SPEED, MAX_SPEED)
        self.rect.center = (x, y)

    def update(self):
        self.x -= self.speed
        self.rect.x = self.x

    def draw(self, surf):
        surf.blit(self.image, self.rect)

fishes = pygame.sprite.Group()