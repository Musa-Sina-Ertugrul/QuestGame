"""
    Pass for linting
"""
# pylint: disable=no-member
# import sys
# pylint: enable=no-member
import pygame

from src.flyweights.animated import Animated

# pylint: disable=no-member
pygame.init()
# pylint: enable=no-member
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
def main():
    """
        Game loop
    """
    while True:
        pygame.display.flip()
        screen.fill((0, 0, 0))
        screen.blit(Animated.data["crazy_chest"][0], (100, 100))
        clock.tick(60)
        raise SystemExit
        # pylint: disable=no-member
        # sys.exit()
        # pylint: enable=no-member
