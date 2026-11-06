import pygame

import game_functions as gf

from settings import Settings
from game_state import GameState
from asset_manager import Images
from button import PlayButton
from dino import Dino
from terrain import Terrain

cd_settings = Settings()

# setup pygame and create screen/clock object
pygame.init()
screen = pygame.display.set_mode((cd_settings.screen_width, cd_settings.screen_height))
clock = pygame.time.Clock()

game_state = GameState(cd_settings)
images = Images()

# creates the dino and terrain
dino = Dino(cd_settings, images.dino_images, screen)
terrain = Terrain(cd_settings, images.terrain_image, screen)

# creates and populates sprite groups
play_button = PlayButton(cd_settings, images.play_button_image, screen)
terrain_sprites = pygame.sprite.Group()
cacti_sprites = pygame.sprite.Group()
terrain_sprites.add(terrain)

while game_state.running :
    gf.check_events(cd_settings, dino, game_state, play_button)

    screen.fill(cd_settings.background_color)

    if game_state.status == "running":
        gf.cacti_spawner(cacti_sprites, cd_settings, game_state, images, screen)
        dino.update()
        gf.update_terrain(cd_settings, images, screen, terrain_sprites)
        gf.update_cacti(cacti_sprites)
        if gf.check_collisions(cacti_sprites, dino):
            gf.reset_game(cacti_sprites, cd_settings, dino, game_state, images, screen, terrain_sprites)

    terrain_sprites.draw(screen)
    cacti_sprites.draw(screen)
    dino.blit_me()
    if game_state.status == "gameover":
        play_button.blit_me()

    pygame.display.flip() # draws the screen object

    clock.tick(cd_settings.max_fps)

pygame.quit()