import pygame
import asset_manager as am
import game_functions as gf

from settings import Settings
from dino import Dino
from terrain import Terrain

cd_settings = Settings()

# setup pygame and create screen/clock object
pygame.init()
screen = pygame.display.set_mode((cd_settings.screen_width, cd_settings.screen_height))
clock = pygame.time.Clock()
running = True

images = am.load_images()

# creates the dino and terrain
dino = Dino(cd_settings, images["dino_images"], screen)
terrain = Terrain(cd_settings, images["terrain_image"], screen)

# creates and populates sprite groups
player_sprites = pygame.sprite.Group()
terrain_sprites = pygame.sprite.Group()
cacti_sprites = pygame.sprite.Group()
player_sprites.add(dino)
terrain_sprites.add(terrain)

while running :
    running = gf.check_events(cacti_sprites, cd_settings, dino, images, screen)

    screen.fill(cd_settings.background_color)

    player_sprites.update()
    gf.update_terrain(cd_settings, images, screen, terrain_sprites)
    gf.update_cacti(cacti_sprites)

    terrain_sprites.draw(screen)
    cacti_sprites.draw(screen)
    player_sprites.draw(screen)

    pygame.display.flip() # draws the screen object

    clock.tick(cd_settings.max_fps)

pygame.quit()