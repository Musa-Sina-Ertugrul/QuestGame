"""sumary_line

Keyword arguments:
argument -- description
Return: return_description

TODO: Update Docstrings

"""

from typing import Tuple, NoReturn
from enum import EnumType
from pygame.camera import Camera
from ..Game import Game



class CameraChild(Game,Camera):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    def __init__(self):
        Game.__init__(self)  # pylint: disable=W,E
        Camera.__init__(self) # TODO: Override most of the methods
        Game.elements = self.init_elements()
        Game.states = self.init_states()

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
