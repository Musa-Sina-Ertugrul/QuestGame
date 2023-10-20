"""sumary_line

Keyword arguments:
argument -- description
Return: return_description

TODO: Update Docstring

"""
from copy import copy
from typing import Tuple, Dict, List, Callable
from enum import EnumType
from pygame import Surface
from ..Menu import Menu


class MenuLabel(Menu):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    def __init__(self):
        super().__init__()
        self.pos_x: int = 0
        self.pos_y: int = 0
        self.elements: List[List[object]] = ((object,),)  # pylint: disable = W,E
        self.internal_states: List[List[Dict]] = [[dict]]
        self.external_states: List[List[Dict]] = [[dict]]

    @property
    def pos_x(self) -> int:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        return self.pos_x

    @pos_x.setter
    def pos_x(self, new_x: int) -> None:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        self.pos_x = new_x

    @property
    def pos_y(self) -> int:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        return self.pos_y

    @pos_y.setter
    def pos_y(self, new_y: int) -> None:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        self.pos_y = new_y

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
        return (self.pos_x, self.pos_y)

    def run(self) -> Tuple[Tuple[Surface]]:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    def init_external_states(self, states: List[List[EnumType]]):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        self.external_states = states

    def init_internal_states(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    def init_elements(  # pylint: disable=W
        self, item_list: Tuple[Tuple[object]]
    ) -> Tuple[Tuple[object]]:  # pylint: disable=W
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        self.elements = item_list

    def update_states(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError
