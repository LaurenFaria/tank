import pygame
import random
# Constants
WIDTH, HEIGHT = 800, 600
tile_size = 64
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Set the display mode

#initilize the fishes group
fishes_group = pygame.sprite.Group()
bullets_group= pygame.sprite.Group()

class Fishes(pygame.sprite.Sprite):
    fish_values = {
        "fishes/orange_fish1.png": 5,
        "fishes/green_fish.png": 3,
        "fishes/yellow_fish.png": 4,
    }
    def __init__(self, image_path, value):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.image = pygame.transform.flip(self.image, True, False)
        self.image.set_colorkey((255, 255, 255))
        self.image.set_colorkey((255,255,255))
        self.rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
        self.velocity = random.uniform(1, 3)
        self.value = value  # Assign specific values to each type of fish
    @classmethod
    def create_background_fish(cls, all_sprites):
        for _ in range(15):
            image_path = random.choice(list(cls.fish_values.keys()))
            fish = cls(image_path, cls.fish_values[image_path])
            all_sprites.add(fish)
    def update(self):
        self.rect.x += self.velocity
        if self.rect.left > WIDTH:
            self.rect.right = 0
# Inside the play_game() function where fish objects are created:
# Create background fish (example)
fish_values = {
    "fishes/orange_fish1.png": 5,
    "fishes/green_fish.png": 3,
    "fishes/yellow_fish.png": 4,
}
for _ in range(10):
    image_path = random.choice(list(fish_values.keys()))
    fish = Fishes(image_path, fish_values[image_path])
    fishes_group.add(fish)

