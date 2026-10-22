import pygame
import asset_manager as am
import game_functions as gf

from settings import Settings
from dino import Dino
from terrain import Ground_Tile
from cacti import Big_Cactus
from cacti import Small_Cactus

cd_settings = Settings()

# setup pygame and create screen/clock object
pygame.init()
screen = pygame.display.set_mode((cd_settings.screen_width, cd_settings.screen_height))
clock = pygame.time.Clock()
running = True

# creates the dino
dino_images = am.load_dino_images()
dino = Dino(cd_settings, dino_images, screen)

# creates the terrain
terrain_image = am.load_terrain_image()
left_tile  = Ground_Tile(cd_settings, terrain_image, screen)
right_tile = Ground_Tile(cd_settings, terrain_image, screen)
right_tile.set_left(left_tile.get_right())

# cacti setup
big_cacti_images = am.load_big_cacti_images()
small_cacti_images = am.load_small_cacti_images()

# creates sprite groups
all_sprites = pygame.sprite.Group()
all_sprites.add(left_tile)
all_sprites.add(right_tile)
all_sprites.add(dino)

cacti = pygame.sprite.Group()


while running :
    # poll for events
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE :
                dino.jump()
            elif event.key == pygame.K_1 :
                new_cactus = Big_Cactus(cd_settings, big_cacti_images, screen, "img1")
                cacti.add(new_cactus)
            elif event.key == pygame.K_2 :
                new_cactus = Big_Cactus(cd_settings, big_cacti_images, screen, "img2")
                cacti.add(new_cactus)
            elif event.key == pygame.K_3 :
                new_cactus = Big_Cactus(cd_settings, big_cacti_images, screen, "img3")
                cacti.add(new_cactus)
            elif event.key == pygame.K_4 :
                new_cactus = Small_Cactus(cd_settings, small_cacti_images, screen, "img1")
                cacti.add(new_cactus)
            elif event.key == pygame.K_5 :
                new_cactus = Small_Cactus(cd_settings, small_cacti_images, screen, "img2")
                cacti.add(new_cactus)
            elif event.key == pygame.K_6 :
                new_cactus = Small_Cactus(cd_settings, small_cacti_images, screen, "img3")
                cacti.add(new_cactus)

    screen.fill(cd_settings.background_color)

    dino.update()
    gf.terrain_update(left_tile, right_tile)
    for cactus in cacti :
        # updates all cacti
        cactus.update()
        # removes cacti off the screen
        if cactus.get_right() < 0 :
            cacti.remove(cactus)

    all_sprites.draw(screen)
    cacti.draw(screen)

    pygame.display.flip() # draws the screen object

    clock.tick(cd_settings.max_fps)

pygame.quit()