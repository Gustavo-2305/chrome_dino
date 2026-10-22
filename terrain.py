import pygame

class Ground_Tile(pygame.sprite.Sprite):
    """A tile of ground"""

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
        self.rect.centery = self.screen_rect.centery + cd_settings.terrainy

    def get_right(self):
        return self.rect.right

    def set_left(self, left):
        self.rect.left = left

    def update(self):
        self.rect.left -= self.speed