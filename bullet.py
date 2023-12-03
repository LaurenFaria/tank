import pygame

WIDTH, HEIGHT = 800, 600
tile_size = 64

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 10  # Bullet speed
        self.direction = pygame.mouse.get_pos()  # Get mouse position

    def update(self):
        # Move the bullet towards the mouse position
        self.rect.x += (self.direction[0] - self.rect.x) * self.speed
        self.rect.y += (self.direction[1] - self.rect.y) * self.speed

        # Remove the bullet when it goes off-screen
        if not pygame.Rect(0, 0, WIDTH, HEIGHT).colliderect(self.rect):
            self.kill()