class Settings() :
    """Stores all settings for the chrome_dino game."""

    def __init__(self):
        self.max_fps = 60

        # screen settings
        self.screen_width = 1280
        self.screen_height = 720
        self.background_color = (255, 255, 255)

        # dino settings
        self.dinoy = (2 * self.screen_height) // 3
        self.animation_speed = 0.15
        self.impulse = 25.0
        self.gravity = 1.7

        # terrain settings
        self.terrainy = (2 * self.screen_height) // 3 + 37
        self.terrain_speed = 15

        #cacti settings
        self.big_cactusy = (2 * self.screen_height) // 3 - 5
        self.small_cactusy = (2 * self.screen_height) // 3 + 10
        self.spawn_waiting_distance = 2 * self.screen_width
        self.spawn_min_interval = self.screen_width // 2
        self.spawn_max_interval = (3 * self.screen_width) // 4