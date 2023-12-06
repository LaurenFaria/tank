import pygame
import random

WIDTH, HEIGHT = 800, 600

class Seamine(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/sprites/seamine.png").convert_alpha()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))

    def update(self):
        pass  # No update logic for the sea mines; they remain stationary

class Bullet(pygame.sprite.Sprite):
    speed = 5  # Adjust the bullet speed as needed

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 5))  # Adjust size and appearance of the bullet
        self.image.fill((255, 0, 0))  # Set color (you can replace this with an image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x += self.speed  # Move bullet horizontally

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    bullets_group = pygame.sprite.Group()
    sea_mines_group = pygame.sprite.Group()

    # Initial number of sea mines
    num_seamines = 5

    # Create initial sea mines
    for _ in range(num_seamines):
        seamine = Seamine()
        all_sprites.add(seamine)
        sea_mines_group.add(seamine)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Increase the number of sea mines gradually
        if pygame.time.get_ticks() % 5000 == 0:  # Adjust timing for increase
            num_seamines += 1
            for _ in range(num_seamines):
                seamine = Seamine()
                all_sprites.add(seamine)
                sea_mines_group.add(seamine)

        # Bullet logic
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            new_bullet = Bullet(WIDTH // 2, HEIGHT // 2)  # Adjust starting position of bullets
            all_sprites.add(new_bullet)
            bullets_group.add(new_bullet)

        # Update bullets
        for bullet in bullets_group:
            bullet.update()

        # Inside the main game loop where you update the bullets and seamines
        bullet_seamine_collisions = pygame.sprite.groupcollide(bullets_group, sea_mines_group, True, True)
        for bullet, seamine_list in bullet_seamine_collisions.items():
            for seamine in seamine_list:
                seamine.kill()

        screen.fill((255, 255, 255))  # Fill screen with a color (replace with your background)
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

