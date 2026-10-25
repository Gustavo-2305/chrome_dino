class Settings() :
    """Stores all settings for the chrome_dino game"""

    def __init__(self):
        self.max_fps = 60

        # screen settings
        self.screen_width = 1280
        self.screen_height = 720
        self.background_color = (255, 255, 255)

        # dino settings
        self.dinoy = (2 * self.screen_height) // 3
        self.animation_speed = 0.15
        self.impulse = 23.0
        self.gravity = 1.3

        # terrain settings
        self.terrainy = (2 * self.screen_height) // 3 + 37
        self.terrain_speed = 15

        #cacti settings
        self.big_cactusy = (2 * self.screen_height) // 3 - 5
        self.small_cactusy = (2 * self.screen_height) // 3 + 10