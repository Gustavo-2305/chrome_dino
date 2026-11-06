class GameState() :
    def __init__(self, cd_settings):
        self.running = True
        self.status = "before_first"
        self.spawn_counter = cd_settings.spawn_waiting_distance