"""
    Pass for linting
"""
# pylint: disable=no-member
import sys

# pylint: enable=no-member
import pygame

from src.flyweights.animated import Animated
from src.Software import Software
from src.factory.Factory import Factory
from src.State import ButtonLookUpTable


def main():
    """
    Game loop
    """

    pygame.init()  # pylint: disable=E

    screen = pygame.display.set_mode((1920, 1080))
    clock = pygame.time.Clock()
    tmp = Factory._create_button(ButtonLookUpTable.SOUND_LEVEL_BUTTON)
    while True:
        pygame.display.flip()
        screen.fill((255, 255, 255))
        surface: pygame.Surface = tmp.run()[0][0]
        rect = surface.get_rect()
        screen.blit(surface, (540 + rect.center[0], 100))
        clock.tick(60)
        # raise SystemExit
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.type == pygame.K_ESCAPE:
                sys.exit(0)


# pylint: disable=all TODO: Check code at below for pointers
def multi(obj):
    print(id(obj[0]))  # TODO: after first run change obj[0] with obj


from multiprocessing import Process
from sys import getsizeof
from copy import copy

if __name__ == "__main__":
    obj = (1, 2, 3)
    p1 = Process(target=multi, args=(obj,))
    p2 = Process(target=multi, args=(obj,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    # NOTE: Check differences with pointers and without pointers
    print("sizeof: " + str(getsizeof(Animated.data)))
    print("sizeof: " + str(getsizeof((Animated.data,))))
    # NOTE: Check these examples
    shallow_copy = copy(obj[1])
    print(id(obj[1]))
    obj = obj[:1] + (4, 5) + obj[2:]
    print(obj)
    print(shallow_copy)
    print(id(shallow_copy))
    shallow_copy = 8
    print(id(shallow_copy))
