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

#pylint: disable=all TODO: Check code at below for pointers
def multi(obj):
    print(id(obj[0])) # TODO: after first run change obj[0] with obj

from multiprocessing import Process
from sys import getsizeof
if __name__ == '__main__':
    obj = (1,2,3)
    p1=Process(target=multi,args=(obj,))
    p2=Process(target=multi,args=(obj,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    # NOTE: Check differences with pointers and without pointers
    print("sizeof: " + str(getsizeof(Animated.data)))
    print("sizeof: " + str(getsizeof((Animated.data,))))
