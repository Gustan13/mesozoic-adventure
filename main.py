import pygame
from settings import arrayMap, WIDTH, HEIGHT, FPS
from drawboard import draw_board
from player import Player
from mainmenu import cutscene
from enemy import Enemy

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
timer = pygame.time.Clock()

# set caption
pygame.display.set_caption('Blue\'s Adventure in the Mesozoic Era')

# sprite groups
collide_tiles, noncollide_tiles, powerup_tiles = draw_board(arrayMap)
player_group = pygame.sprite.GroupSingle()
player = Player(64, 64, 64, 64, collide_tiles)
player_group.add(player)

enemy_group = pygame.sprite.Group()
enemy_1 = Enemy('eoraptor', 320, 320, 64, 64, 10, 0.5)
enemy_2 = Enemy('ptedoaustro', 192, 896, 64, 64, 10, 0.5)
enemy_3 = Enemy('yi qi', 896, 256, 64, 64, 10, 0.5)
enemy_group.add(enemy_1, enemy_2, enemy_3)


def main():
    cutscene(screen)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill('black')

        collide_tiles.draw(screen)
        # noncollide_tiles.draw(screen)
        # powerup_tiles.draw(screen)

        player_group.draw(screen)
        player_group.update()

        enemy_group.draw(screen)
        enemy_group.update(arrayMap, player)

        timer.tick(FPS)
        pygame.display.update()  # update the display

    pygame.display.quit()
    pygame.quit()


if __name__ == '__main__':  # if the file is run directly
    main()
