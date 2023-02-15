import pygame
from settings import *

PATH = 0
WALL = 1
INVINCIBLE = 2
ZAWARUDO = 3

class CollideTile(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.id = "WALL"


class PowerUpTile(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, type):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.id = "POWERUP"
        self.type_of_powerup = type

    def kill(self, collide_tiles):
        collide_tiles.remove(self)


class NonCollideTiles(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.id = "PATH"
        

def draw_board(level):
    # each block should have a width of 30 pixels and a height of 30 pixels
    # (the board should be 30 blocks wide and 30 blocks high)
    # create new sprite group
    collide_tiles = pygame.sprite.Group()
    noncollide_tiles = pygame.sprite.Group()
    # loop through level array
    for row in range(len(level)):
        for col in range(len(level[row])):
            if level[row][col] == WALL:
                collide_tiles.add(CollideTile(
                    col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE, 'black'))
                continue
            elif level[row][col] == PATH:
                collide_tiles.add(PowerUpTile(
                    col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE, 'green', 'pellet'))
            elif level[row][col] == INVINCIBLE:
                collide_tiles.add(PowerUpTile(
                    col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE, 'blue', 'invincibilidade'))
            elif level[row][col] == ZAWARUDO:
                collide_tiles.add(PowerUpTile(
                    col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE, 'red', 'invincibilidade'))
            noncollide_tiles.add(NonCollideTiles(
                    col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE, 'white'))

    return collide_tiles, noncollide_tiles
