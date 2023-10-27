"""sumary_line

Keyword arguments:
argument -- description
Return: return_description

TODO: Update Docstrings

"""
from sys import path
from typing import Tuple, List, Final, Dict  # pylint: disable=W,E
from pygame import Surface, transform  # pylint: disable=W,E

path.append("main/src/flyweights")
path.append("main/src/")

from not_animated import (  # pylint: disable=W,E,import-error,wrong-import-position
    NotAnimated,  # pylint: disable=W,E,import-error,wrong-import-position
)  # pylint: disable=W,E,import-error,wrong-import-position
from State import (  # pylint: disable=W,E,import-error,wrong-import-position
    StateLookUpTable,  # pylint: disable=W,E,import-error,wrong-import-position
)  # pylint: disable=W,E,import-error,wrong-import-position
from ..Menu import Menu  # pylint: disable=W,E,import-error,wrong-import-position


class Icon(Menu):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    def __init__(self):
        super().__init__(self)  # pylint: disable=W,E
        self.elements: Tuple[Tuple[object]] = ((object,),)  # pylint: disable = W,E
        self.internal_states: Tuple[Tuple[Dict]] = ((dict,),)
        self.external_states: Tuple[Tuple[Dict]] = ((dict,),)

    @property
    def pos_x(self) -> int:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        return self().pos_x

    @pos_x.setter
    def pos_x(self, new_x: int) -> None:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        self().pos_x = new_x

    @property
    def pos_y(self) -> int:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        return self().pos_y

    @pos_y.setter
    def pos_y(self, new_y: int) -> None:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        self().pos_y = new_y

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

    def update_elements(self) -> None:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    def notify_states(self) -> None:
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
        return (self._x, self._y)

    def run(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    def init_external_states(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    def init_internal_states(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    def init_elements(self, icon: int) -> Tuple[Tuple[object]]:  # pylint: disable=W
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    def __change_color(self) -> None:  # pylint: disable=W
        raise NotImplementedError

    def update_states(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError
