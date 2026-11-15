class Scoreboard():

    def __init__(self, cd_settings, font):
        self.cd_settings = cd_settings
        self.font = font

        self.increase_per_frame = cd_settings.increase_per_frame
        self.font_spacing = cd_settings.font_spacing
        self.scoreboardx = cd_settings.scoreboardx
        self.scoreboardy = cd_settings.scoreboardy
        
        self.score_float = 0.0
        self.score = 0
        self.hi_score = 0

    def update(self):
        self.score_float += self.increase_per_frame
        self.score = int(self.score_float)

    def reset(self):
        if (self.score > self.hi_score):
            self.hi_score = self.score
        self.score_float = 0.0
        self.score = 0

    def render(self):
        score_str = f"{self.score:05d}"
        hi_score_str = f"{self.hi_score:05d}"
        combined_str = "HI " + hi_score_str + " " + score_str
        return self.font.render(combined_str, self.cd_settings.font_spacing)