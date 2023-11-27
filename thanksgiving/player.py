import pygame
import random

#setting the parameters
WIDTH, HEIGHT = 800, 600
tile_size = 64
PLAYER_SPEED =
class Fish(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image.set_colorkey((255,255,255))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
        self.speed = 3

    # Creating the player fish controls
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

    def move_up(self):
        self.y_speed = -1*PLAYER_SPEED
    def move_down(self):
        self.y_speed = PLAYER_SPEED
    def move_left(self):
        self.x_speed = -1*PLAYER_SPEED
        self.image = self.reverse_image
    def move_right(self):
        self.x_speed = PLAYER_SPEED
        self.image = self.forward_image

    def stop(self):
        self.x_speed = 0
        self.y_speed = 0
    def update(self):
        #TODO: need to check in the player went off of the screen
        self.x += self.x_speed
        self.y += self.y_speed
        self.rect.x = self.x
        self.rect.y = self.y
        if self.rect.x > screen_width - self.rect.width:
            self.x_speed = 0
        if self.rect.y > screen_height-self.rect.height:
            self.y_speed = 0
        if self.rect.x < 0:
            self.x_speed = 0
        if self.rect.y < 0:
            self.y_speed = 0


    def draw(self,surf):
        surf.blit(self.image, self.rect)