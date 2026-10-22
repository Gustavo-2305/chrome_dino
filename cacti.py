import pygame

class Big_Cactus(pygame.sprite.Sprite):
    """An individual cactus"""

    def __init__(self, cd_settings, cacti_images, screen, type):
        super().__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()

        # loads images and creates rects
        self.image = cacti_images[type]
        self.rect = self.image.get_rect()

        # sets starting position and speed
        self.speed = cd_settings.terrain_speed
        self.rect.left = self.screen_rect.right
        self.rect.centery = self.screen_rect.centery + cd_settings.bigcactusy

    def get_right(self):
        return self.rect.right

    def update(self):
        self.rect.left -= self.speed

class Small_Cactus(pygame.sprite.Sprite):
    """An individual cactus"""

    def __init__(self, cd_settings, cacti_images, screen, type):
        super().__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()

        # loads images and creates rects
        self.image = cacti_images[type]
        self.rect = self.image.get_rect()

        # sets starting position and speed
        self.speed = cd_settings.terrain_speed
        self.rect.left = self.screen_rect.right
        self.rect.centery = self.screen_rect.centery + cd_settings.smallcactusy

    def get_right(self):
        return self.rect.right

    def update(self):
        self.rect.left -= self.speed