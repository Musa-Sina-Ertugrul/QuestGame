"""
    Pass for linting
"""
# pylint: disable=no-member
# import sys
# pylint: enable=no-member
import pygame

from src.flyweights.animated import Animated


def main():
    """
    Game loop
    """

    pygame.init()  # pylint: disable=E

    screen = pygame.display.set_mode((800, 800))
    clock = pygame.time.Clock()
    while True:
        pygame.display.flip()
        screen.fill((0, 0, 0))
        screen.blit(Animated.data["crazy_chest"][0], (100, 100))
        clock.tick(60)
        raise SystemExit
        # pylint: disable=no-member
        # sys.exit()
        # pylint: enable=no-member
