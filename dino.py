import pygame

class Dino(pygame.sprite.Sprite):
    """The dinossaur character controlled by the player"""

    def __init__(self, cd_settings, dino_images, screen):
        super().__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()

        # loads settings
        self.animation_speed = cd_settings.animation_speed
        self.gravity = cd_settings.gravity
        self.impulse = cd_settings.impulse

        # loads images and creates rects
        self.walk_images = dino_images["walk"]
        self.jump_image = dino_images["jump"]
        self.frame = 0.0
        self.image = self.walk_images[int(self.frame)]
        self.rect = self.image.get_rect()

        self.state = "running"

        # sets starting position and speed
        self.rect.left = self.rect.width
        self.rect.centery = self.screen_rect.centery
        self.vertical_position = 0.0
        self.vertical_speed = 0.0

    def update(self):
        if self.state == "running":
            self.update_animation()
        elif self.state == "jumping":
            self.update_position()

    def update_animation(self):
        self.frame += self.animation_speed
        if self.frame >= len(self.walk_images): # loops to the first frame at the end
            self.frame = 0.0

        self.image = self.walk_images[int(self.frame)]

    def update_position(self):
        self.vertical_position += self.vertical_speed
        if self.vertical_position > 0:
            self.vertical_speed -= self.gravity
        else:
            self.vertical_position = 0
            self.state = "running"
        self.rect.centery = self.screen_rect.centery - int(self.vertical_position)

    def jump(self):
        if self.state != "jumping":
            self.state = "jumping"
            self.vertical_speed = self.impulse

            # changes to the midjump image
            self.image = self.jump_image

    def blitme(self):
        # draws the dino into the screen
        self.screen.blit(self.image, self.rect)