"""sumary_line

Keyword arguments:
argument -- description
Return: return_description

TODO: Update Docstrings

"""
from sys import path
from typing import Tuple, NoReturn, List, Final, Dict  # pylint: disable=W,E
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
        super.elements: Tuple[
            Tuple[object]
        ] = ((object,),) # pylint: disable = W,E
        super.internal_states: Tuple[Tuple[Dict]] = ((dict,),)
        super.external_states: Tuple[Tuple[Dict]] = ((dict,),)

    @property
    def pos_x(self) -> int:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        return super().pos_x

    @pos_x.setter
    def pos_x(self, new_x: int) -> NoReturn:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        super().pos_x = new_x

    @property
    def pos_y(self) -> int:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        return super().pos_y

    @pos_y.setter
    def pos_y(self, new_y: int) -> NoReturn:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        super().pos_y = new_y

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

    def __change_color(self) -> NoReturn:  # pylint: disable=W
        raise NotImplementedError

    def update_states(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError
