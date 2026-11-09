import pygame

class GameOver(pygame.sprite.Sprite):
    """The game over text."""

    def __init__(self, cd_settings, text_images, screen):
        super().__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()

        # loads image and creates rect
        self.image = text_images.game_over
        self.rect = self.image.get_rect()

        # positions the button
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = cd_settings.game_overy

    def blit_me(self):
        # draws the button to the screen
        self.screen.blit(self.image, self.rect)