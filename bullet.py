import pygame
from seamine import Seamine

WIDTH, HEIGHT = 800, 600

class Bullet(pygame.sprite.Sprite):
    speed = 5  # Adjust the bullet speed as needed
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/sprites/bubble.png").convert_alpha()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x += self.speed  # Move bullet horizontally

    def draw(self, screen):
        screen.blit(self.image, self.rect)

bullets_group = pygame.sprite.Group()  # Create a group to hold bullets
sea_mines_group = pygame.sprite.Group()

def shoot(player):
    # Define the number of bullets to shoot at once
    num_bullets = 0.5  # Adjust the number of bullets as needed

    for _ in range(num_bullets):
        new_bullet = Bullet(player.rect.right, player.rect.centery)
        bullets_group.add(new_bullet)