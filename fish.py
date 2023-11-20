
# create a pygame sprite class for a fish
import random
import pygame

MIN_SPEED = .5
MAX_SPEED = 3
class Fish(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load('assets/sprites/green_fish.png')
        self.image.set_colorkey((0,0,0))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect - self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = random.uniform(MIN_SPEED, MAX_SPEED)
        self.rect.center = (x,y)

    def update(self):
        self.x -=self.speed
        self.rect.x = self.x
    def draw(self, surf):
        surf.blit(self.image, self.rect)

fishes = pygame.sprite.Group()