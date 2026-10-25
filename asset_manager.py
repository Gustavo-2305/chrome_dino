import pygame

class Images():
    """Stores all image assets."""

    def __init__(self):
        self.dino_images = DinoImages()
        self.terrain_image = pygame.image.load('images/terrain.png').convert_alpha()
        self.cacti_images = CactiImages()

    def load_cacti_images():
        images = {}

        

        return images

class DinoImages():
    """Stores all dino images."""

    def __init__(self):
        self.walk = [
            pygame.image.load('images/walk0.png').convert_alpha(),
            pygame.image.load('images/walk1.png').convert_alpha()
        ]
        self.jump = pygame.image.load('images/jump0.png').convert_alpha()

class CactiImages():
    """Stores all cacti images."""

    def __init__(self):
        self.big1 = pygame.image.load('images/big_cactus1.png').convert_alpha()
        self.big2 = pygame.image.load('images/big_cactus2.png').convert_alpha()
        self.big3 = pygame.image.load('images/big_cactus3.png').convert_alpha()
        self.small1 = pygame.image.load('images/small_cactus1.png').convert_alpha()
        self.small2 = pygame.image.load('images/small_cactus2.png').convert_alpha()
        self.small3 = pygame.image.load('images/small_cactus3.png').convert_alpha()