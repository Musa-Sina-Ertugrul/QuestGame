"""sumary_line

Keyword arguments:
argument -- description
Return: return_description

TODO: Update Docstrings

"""

from typing import Tuple, NoReturn
from enum import EnumType
from sys import path
from numpy import random
from pygame import Surface

path.append("main/src/flyweights/")
from not_animated import NotAnimated #pylint: disable=import-error,wrong-import-position
from ..Menu import Menu #pylint: disable=wrong-import-position


class MainMenu(Menu):
    """sumary_line
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    def __init__(self):
        super().__init__(self) # pylint: disable=W,E
        self.bg_random : Tuple[Surface] = (NotAnimated.data["bgs_main_menu"][int(random.uniform(low=0.0,high=4.999))])
        super.elememts = self.init_elements()
        super.states = self.init_states()

    def relative_pos(self) -> Tuple[int, int]:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    def relative_height(self) -> int:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    def relative_width(self) -> int:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    def update_elements(self) -> NoReturn:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    def notify_states(self) -> NoReturn:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    def current_pos(self) -> Tuple[int, int]:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        if NotImplemented:
            raise NotImplementedError
        return (self._x, self._y)

    def run(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    def init_states(self) -> Tuple[Tuple[EnumType]]:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    def init_elements(self) -> Tuple[Tuple[object]]:  # pylint: disable=W
        """sumary_line
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError
