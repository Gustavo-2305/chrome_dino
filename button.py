class PlayButton():

    def __init__(self, cd_settings, play_button_image, screen):
        """The play button used to restart the game"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # loads image and creates rect
        self.image = play_button_image
        self.rect = self.image.get_rect()

        # positions the button
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = cd_settings.buttony

    def blit_me(self):
        # draws the button to the screen
        self.screen.blit(self.image, self.rect)
