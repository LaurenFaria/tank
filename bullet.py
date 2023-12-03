import pygame
from seamine import Seamine

WIDTH, HEIGHT = 800, 600

class Bullet(pygame.sprite.Sprite):
    speed = 5  # Adjust the bullet speed as needed
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 1))  # Adjust size as needed
        self.image.fill((0, 255, 0))  # Green bullet
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x += self.speed  # Move bullet horizontally

    def draw(self, screen):
        screen.blit(self.image, self.rect)

bullets = pygame.sprite.Group()  # Create a group to hold bullets
sea_mines_group = pygame.sprite.Group()

def shoot(player):
    new_bullet = Bullet(player.rect.right, player.rect.centery)
    bullets.add(new_bullet)



