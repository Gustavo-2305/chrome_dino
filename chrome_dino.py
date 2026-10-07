import pygame

from settings import Settings
from dino import Dino

cd_settings = Settings()

# setup pygame and create screen/clock object
pygame.init()
screen = pygame.display.set_mode((cd_settings.screen_width, cd_settings.screen_height))
clock = pygame.time.Clock()
running = True

# creates the dino
dino = Dino(screen, cd_settings)

while running :
    # poll for events
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE :
                dino.jump()

    screen.fill(cd_settings.background_color)

    dino.update()
    dino.blitme()

    pygame.display.flip() # draws the screen object

    clock.tick(cd_settings.max_fps)

pygame.quit()