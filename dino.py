import pygame

class Dino():
    """The dinossaur character controlled by the player"""

    def __init__(self, screen, cd_settings):
        # loads settings
        self.screen = screen
        self.animation_speed = cd_settings.animation_speed
        self.gravity = cd_settings.gravity
        self.impulse = cd_settings.impulse
        self.state = "running"

        # loads images and creates rects
        self.walk_images = [
            pygame.image.load('images/walk0.png').convert_alpha(),
            pygame.image.load('images/walk1.png').convert_alpha()
        ]
        self.jump_image = pygame.image.load('images/jump0.png').convert_alpha()
        self.frame = 0.0
        self.image = self.walk_images[int(self.frame)]
        self.dino_rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # sets starting position and speed
        self.dino_rect.left = self.dino_rect.width
        self.dino_rect.centery = self.screen_rect.centery
        self.vertical_position = 0.0
        self.vertical_speed = 0.0

    def update(self):
        if self.state == "running":
            self.update_animation()
        elif self.state == "jumping":
            self.update_position()

    def update_animation(self):
        old_center = self.dino_rect.center
        self.frame += self.animation_speed
        if self.frame >= len(self.walk_images): # loops to the first frame at the end
            self.frame = 0.0
        self.image = self.walk_images[int(self.frame)]
        self.dino_rect = self.image.get_rect(center = old_center)

    def update_position(self):
        self.vertical_position += self.vertical_speed
        if self.vertical_position > 0:
            self.vertical_speed -= self.gravity
        else:
            self.vertical_position = 0
            self.state = "running"
        self.dino_rect.centery = self.screen_rect.centery - int(self.vertical_position)

    def jump(self):
        if self.state != "jumping" :
            self.state = "jumping"
            self.vertical_speed = self.impulse

            # changes to the midjump image
            old_center = self.dino_rect.center
            self.image = self.jump_image
            self.dino_rect = self.image.get_rect(center = old_center)

    def blitme(self):
        # draws the dino into the screen
        self.screen.blit(self.image, self.dino_rect)