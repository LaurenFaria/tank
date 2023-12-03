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
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    # Initial number of sea mines
    num_seamines = 5
    # Create initial sea mines
    for _ in range(num_seamines):
        seamine = Seamine()
        all_sprites.add(seamine)
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
        screen.fill((255, 255, 255))  # Fill screen with blue color for example
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
if __name__ == "__main__":
    main()
    main()
