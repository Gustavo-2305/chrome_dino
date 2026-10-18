import pygame

class Terrain(pygame.sprite.Sprite):
    """The terrain and the cacti"""

    def __init__(self, cd_settings, terrain_image, screen):
        super().__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()

        # loads images and creates rects
        self.image = terrain_image
        self.rect = self.image.get_rect()

        # sets starting position
        self.rect.left = 0
        self.rect.centery = self.screen_rect.centery + cd_settings.terrainy