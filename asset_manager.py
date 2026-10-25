import pygame

def load_images():
    """Loads all images assets into a dictionary."""
    images = {}

    images["dino_images"] = load_dino_images()
    images["terrain_image"] = load_terrain_image()
    images["cacti_images"] = load_cacti_images()

    return images

def load_dino_images():
    images = {}

    images["walk"] = [
        pygame.image.load('images/walk0.png').convert_alpha(),
        pygame.image.load('images/walk1.png').convert_alpha()
    ]
    images["jump"] = pygame.image.load('images/jump0.png').convert_alpha()

    return images

def load_terrain_image():
    image = pygame.image.load('images/terrain.png').convert_alpha()

    return image

def load_cacti_images():
    images = {}

    images["big1"] = pygame.image.load('images/big_cactus1.png').convert_alpha()
    images["big2"] = pygame.image.load('images/big_cactus2.png').convert_alpha()
    images["big3"] = pygame.image.load('images/big_cactus3.png').convert_alpha()
    images["small1"] = pygame.image.load('images/small_cactus1.png').convert_alpha()
    images["small2"] = pygame.image.load('images/small_cactus2.png').convert_alpha()
    images["small3"] = pygame.image.load('images/small_cactus3.png').convert_alpha()

    return images