"""
    This file contains Flyweights as Prototype
    Flyweight class is an abstract class it has been
    inhereted by Animated and Not_Animated classes
    These two classes will contain assests as static
"""

from abc import ABC
from typing import Dict, List, Optional
from pygame import Surface
from pygame.mixer import Sound
from pygame.font import Font


class Flyweight(ABC):
    """
    Data container for Flyweight objects

    This class is an abstract class and is inhereted by Animeted
    and NotAnimated classes

    Attributes:
        data (Dict[str, List[Surface]]) : contains Surface objects
    """

    data: Dict[str, List[Optional[Font | Sound | Surface]]] = {}






