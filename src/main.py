import pygame
from player import Player
from oxygen import OxygenSystem
from treasure import TreasureManager
from enemy import EnemyManager
from settings import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Treasure Dive")

clock = pygame.time.Clock()

player = Player()
oxygen = OxygenSystem()
treasures = TreasureManager()
enemies = EnemyManager()

running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    player.update()
    oxygen.update(player)
    treasures.update()
    enemies.update()

    treasures.check_collection(player)
    enemies.check_collision(player)

    # Draw
    screen.fill((0, 100, 200))

    player.draw(screen)
    treasures.draw(screen)
    enemies.draw(screen)
    oxygen.draw(screen)

    pygame.display.flip()

pygame.quit()
