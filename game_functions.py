import pygame
import random

import cacti as ca

from terrain import Terrain

random.seed()

def check_events(cd_settings, dino):
    # checks for player inputs

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            return False
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE :
                dino.jump()
                

    return True

def cacti_spawner(cacti_sprites, cd_settings, images, screen, spawn_counter):
    # spawns the cacti
    if spawn_counter < 0:
        type = random.randint(0, 5)
        spawn_counter = random.randint(cd_settings.spawn_min_interval, cd_settings.spawn_max_interval)

        if type == 0 :
            new_cactus = ca.BigCactus1(images.cacti_images, cd_settings, screen)
            cacti_sprites.add(new_cactus)
        elif type == 1 :
            new_cactus = ca.BigCactus2(images.cacti_images, cd_settings, screen)
            cacti_sprites.add(new_cactus)
        elif type == 2 :
            new_cactus = ca.BigCactus3(images.cacti_images, cd_settings, screen)
            cacti_sprites.add(new_cactus)
        elif type == 3 :
            new_cactus = ca.SmallCactus1(images.cacti_images, cd_settings, screen)
            cacti_sprites.add(new_cactus)
        elif type == 4 :
            new_cactus = ca.SmallCactus2(images.cacti_images, cd_settings, screen)
            cacti_sprites.add(new_cactus)
        elif type == 5 :
            new_cactus = ca.SmallCactus3(images.cacti_images, cd_settings, screen)
            cacti_sprites.add(new_cactus)

    return spawn_counter - cd_settings.terrain_speed

def update_terrain(cd_settings, images, screen, terrain_sprites):
    # updates terrain objects, adds and remove them as necessary

    terrain_sprites.update()
    if (len(terrain_sprites) == 1):
        new_terrain = Terrain(cd_settings, images.terrain_image, screen)
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