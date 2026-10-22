class Settings() :
    """Stores all settings for the chrome_dino game"""

    def __init__(self):
        self.max_fps = 60
        # screen settings
        self.screen_width = 1280
        self.screen_height = 720
        self.background_color = (255, 255, 255)
        # dino settings
        self.animation_speed = 0.15
        self.impulse = 22.0
        self.gravity = 1.3
        # terrein settings
        self.terrainy = 37 # from screen.centery
        self.terrain_speed = 10
        #cactus setting
        self.bigcactusy = -5 # from screen.centery
        self.smallcactusy = 10 # from screen.centery