"""sumary_line

Keyword arguments:
argument -- description
Return: return_description

TODO: Update Docstrings

"""
from copy import copy
from enum import EnumType
from typing import Tuple, Callable, Dict, List
from time import sleep
from pygame import Surface, transform
from src.State import ButtonStateLookUpTable
from ..Menu import Menu


class Button(Menu):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    def __init__(self):
        self.elements: List[List[object]] = [[object]]  # pylint: disable = W,E
        self.internal_states: List[List[EnumType]] = [[dict]]
        self.external_states: List[List[EnumType]] = [[dict]]
        self.functionality: Callable = None
        self.size_nultiplier: float = 1.0

    @property
    def __func(self) -> Callable:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        return self.functionality

    @__func.setter
    def set_func(self, func: Callable) -> None:
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
        """draw other elements on label surface

        This method returns first elements on label surface
        (first elements) to be draw on other surfaces

        Return:
            Tuple[Tuple[Surface]] : returns label surface as ptr
        """
        final_elements = [
            [self.elements[0][i].run()[0][0], self.elements[0][i].relative_pos()]
            for i in range(1, len(self.elements[0]))
        ]
        base_label: Surface = copy(self.elements[0][0])
        base_label.fill((255, 0, 0))
        base_label.blits(blit_sequence=final_elements)
        base_label = transform.scale_by(base_label, self.size_nultiplier)
        self.functionality()
        self.update_states()
        return ((base_label,),)

    def init_external_states(self, states: List[List[EnumType]]) -> None:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        self.external_states = states

    def init_internal_states(self, states: List[List[EnumType]]) -> None:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        self.internal_states = states

    def init_elements(self, elements: List[List[object]]) -> None:
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
        for i in range(len(self.elements[0])):
            match self.external_states[0][i]:
                case ButtonStateLookUpTable.NULL:
                    continue
                case ButtonStateLookUpTable.CLICKED:
                    self.elements[0][i].set_mouse_state = ButtonStateLookUpTable.CLICKED
                case ButtonStateLookUpTable.ON_CLICK:
                    self.elements[0][
                        i
                    ].set_mouse_state = ButtonStateLookUpTable.ON_CLICK
                case ButtonStateLookUpTable.NOT_COLLIDE:
                    self.elements[0][
                        i
                    ].set_mouse_state = ButtonStateLookUpTable.NOT_COLLIDE
                case _:
                    raise RuntimeError(
                        f"Wrong state {self.external_states[0][i].__name__}"
                    )
