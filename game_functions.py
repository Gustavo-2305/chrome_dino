import pygame
import random

import cacti as ca

from terrain import Terrain

random.seed()

def check_events(cd_settings, dino, game_state, play_button):
    # checks for player inputs
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            game_state.running = False
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE :
                if game_state.status == "running":
                    dino.jump()
                elif game_state.status == "before_first":
                    game_state.status = "running"
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousex, mousey = pygame.mouse.get_pos()
            check_play_button(game_state, play_button, mousex, mousey)

def check_play_button(game_state, play_button, mousex, mousey) :
    # checks if the play button was clicked
    if game_state.status == "gameover" and play_button.rect.collidepoint(mousex, mousey):
        game_state.status = "running"

def cacti_spawner(cacti_sprites, cd_settings, game_state, images, screen):
    # spawns the cacti
    if game_state.spawn_counter < 0:
        type = random.randint(0, 5)
        game_state.spawn_counter = random.randint(cd_settings.spawn_min_interval, cd_settings.spawn_max_interval)

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

    game_state.spawn_counter -= cd_settings.terrain_speed

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

def check_collisions(cacti_sprites, dino):
    # checks and handles collisions between the dino and the cacti
    collisions = pygame.sprite.spritecollideany(dino, cacti_sprites)

    if collisions:
        return True

    return False

def reset_game(cacti_sprites, cd_settings, dino, game_state, images, screen, terrain_sprites):
    # resets the whole game
    dino.vertical_position = 0
    dino.rect.centery = cd_settings.dinoy
    dino.image = dino.jump_image

    terrain_sprites.empty()
    terrain = Terrain(cd_settings, images.terrain_image, screen)
    terrain_sprites.add(terrain)

    cacti_sprites.empty()

    game_state.spawn_counter = cd_settings.spawn_waiting_distance
    game_state.status = "gameover"