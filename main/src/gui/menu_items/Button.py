"""sumary_line

Keyword arguments:
argument -- description
Return: return_description

TODO: Update Docstrings

"""
from copy import copy
from enum import EnumType
from typing import Tuple, NoReturn, Callable, Dict, List
from pygame import Surface
from ..Menu import Menu


class Button(Menu):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    def __init__(self):
        super().__init__(self)  # pylint: disable=W,E
        self.elements: List[
            List[object]
        ] = [[object]] # pylint: disable = W,E
        self.internal_states: List[List[Dict]] = [[dict]]
        self.external_states: List[List[Dict]] = [[dict]]
        self.functionality: Callable = None

    @property
    def __func(self)-> Callable:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        return self.functionality

    @__func
    def set_func(self,func : Callable) -> None:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        self.functionality = func

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
        return (self.pos_x, self.pos_y)

    def run(self) -> Tuple[Tuple[Surface]]:
        """draw other elements on label surface

        This method returns first elements on label surface 
        (first elements) to be draw on other surfaces

        Return:
            Tuple[Tuple[Surface]] : returns label surface as ptr
        """
        final_elements = [self.elements[0][i].run() for i in range(len(self.elements[0][1:]))]
        base_label : Surface = copy(self.elements[0][0])
        base_label.blits(final_elements)

        return ((base_label,),)

    def init_external_states(self,states : List[List[EnumType]]) -> None:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        self.external_states = states

    def init_internal_states(self,states : List[List[EnumType]]) -> None:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        self.internal_states = states

    def init_elements(self, elements : List[List[object]]) -> None:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        self.elements = elements

    def update_states(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError
