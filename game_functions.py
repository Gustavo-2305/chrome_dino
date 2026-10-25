import pygame
import cacti as ca

from terrain import Terrain

def check_events(cacti_sprites, cd_settings, dino, images, screen):
    # checks for player inputs

    for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                return False
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE :
                    dino.jump()
                elif event.key == pygame.K_1 :
                    new_cactus = ca.BigCactus1(images["cacti_images"], cd_settings, screen)
                    cacti_sprites.add(new_cactus)
                elif event.key == pygame.K_2 :
                    new_cactus = ca.BigCactus2(images["cacti_images"], cd_settings, screen)
                    cacti_sprites.add(new_cactus)
                elif event.key == pygame.K_3 :
                    new_cactus = ca.BigCactus3(images["cacti_images"], cd_settings, screen)
                    cacti_sprites.add(new_cactus)
                elif event.key == pygame.K_4 :
                    new_cactus = ca.SmallCactus1(images["cacti_images"], cd_settings, screen)
                    cacti_sprites.add(new_cactus)
                elif event.key == pygame.K_5 :
                    new_cactus = ca.SmallCactus2(images["cacti_images"], cd_settings, screen)
                    cacti_sprites.add(new_cactus)
                elif event.key == pygame.K_6 :
                    new_cactus = ca.SmallCactus3(images["cacti_images"], cd_settings, screen)
                    cacti_sprites.add(new_cactus)

    return True

def update_terrain(cd_settings, images, screen, terrain_sprites):
    # updates terrain objects, adds and remove them as necessary

    terrain_sprites.update()
    if (len(terrain_sprites) == 1):
        new_terrain = Terrain(cd_settings, images["terrain_image"], screen)
        old_terrain = terrain_sprites.sprites()[0]
        new_terrain.rect.left = old_terrain.rect.right
        terrain_sprites.add(new_terrain)
    for terrain in terrain_sprites:
        if terrain.rect.right < 0:
            terrain_sprites.remove(terrain)

def update_cacti(cacti_sprites):
    # updates cacti objects and remove them as necessary
    cacti_sprites.update()

    for cactus in cacti_sprites:
        if cactus.rect.right < 0:
            cacti_sprites.remove(cactus)