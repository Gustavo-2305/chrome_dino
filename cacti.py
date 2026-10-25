import pygame

class Cactus(pygame.sprite.Sprite):
    """Base class for all cactus obstacles."""

    def __init__(self, cactus_image, cactusy, cd_settings, screen):
        super().__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()
        # loads images and creates rects
        self.image = cactus_image
        self.rect = self.image.get_rect()
        # sets starting position and speed
        self.speed = cd_settings.terrain_speed
        self.rect.left = self.screen_rect.right
        self.rect.centery = cactusy

    def update(self):
        self.rect.left -= self.speed

class BigCactus1(Cactus):
    """One big cactus."""

    def __init__(self, cacti_images, cd_settings, screen):
        super().__init__(cacti_images.big1, cd_settings.big_cactusy, cd_settings, screen)

class BigCactus2(Cactus):
    """Two big cacti."""

    def __init__(self, cacti_images, cd_settings, screen):
        super().__init__(cacti_images.big2, cd_settings.big_cactusy, cd_settings, screen)

class BigCactus3(Cactus):
    """Three big cacti."""

    def __init__(self, cacti_images, cd_settings, screen):
        super().__init__(cacti_images.big3, cd_settings.big_cactusy, cd_settings, screen)

class SmallCactus1(Cactus):
    """One small cactus."""

    def __init__(self, cacti_images, cd_settings, screen):
        super().__init__(cacti_images.small1, cd_settings.small_cactusy, cd_settings, screen)

class SmallCactus2(Cactus):
    """Two small cacti."""

    def __init__(self, cacti_images, cd_settings, screen):
        super().__init__(cacti_images.small2, cd_settings.small_cactusy, cd_settings, screen)

class SmallCactus3(Cactus):
    """Three small cacti."""

    def __init__(self, cacti_images, cd_settings, screen):
        super().__init__(cacti_images.small3, cd_settings.small_cactusy, cd_settings, screen)