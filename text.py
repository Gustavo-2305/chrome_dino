import pygame

class CustomFont():
    """Creates a custom font with a PNG image"""

    def __init__(self, image_path, char_width, char_height, characters):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.char_width = char_width
        self.char_height = char_height
        self.characters = characters
        self.glyphs = {}
        self.load_glyphs()

    def load_glyphs(self):
        for index, char in enumerate(self.characters):
            x = index * self.char_width
            y = 0
            rect = pygame.Rect(x, y, self.char_width, self.char_height)
            self.glyphs[char] = self.image.subsurface(rect).copy()

    def render(self, text, spacing=0):
        width = len(text) * (self.char_width + spacing)
        height = self.char_height
        surface = pygame.Surface((width, height), pygame.SRCALPHA)
        x = 0
        for char in text:
            if char in self.glyphs:
                surface.blit(self.glyphs[char], (x, 0))
            x += self.char_width + spacing

        return surface


class GameOver():
    """The game over text."""

    def __init__(self, cd_settings, text_images, screen):
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
