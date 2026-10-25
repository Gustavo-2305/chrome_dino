import pygame

class Terrain(pygame.sprite.Sprite):
    """A section of terrain."""

    def __init__(self, cd_settings, terrain_image, screen):
        super().__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()
        # loads images and creates rects
        self.image = terrain_image
        self.rect = self.image.get_rect()
        # sets starting position and speed
        self.speed = cd_settings.terrain_speed
        self.rect.left = 0
        self.rect.centery = cd_settings.terrainy

    def update(self):
        self.rect.left -= self.speed