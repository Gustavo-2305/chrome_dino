import pygame

def load_dino_images():
    images = {}

    images["walk"] = [
        pygame.image.load('images/walk0.png').convert_alpha(),
        pygame.image.load('images/walk1.png').convert_alpha()
    ]
    images["jump"] = pygame.image.load('images/jump0.png').convert_alpha()

    return images