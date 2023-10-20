"""sumary_line

Keyword arguments:
argument -- description
Return: return_description

TODO: Update Docstrings

"""
from sys import path
from typing import Tuple, Dict, List, Callable
from copy import copy
from functools import lru_cache
from enum import EnumType
from pygame.font import Font
from pygame import Surface
from pygame import transform

path.append("main/src/flyweights")
path.append("main/src/")

from not_animated import (  # pylint: disable=W,E,import-error,wrong-import-position
    NotAnimated,
)
from State import (  # pylint: disable=W,E,import-error,wrong-import-position
    StateLookUpTable,
)
from ..Menu import Menu  # pylint: disable=W,E,import-error,wrong-import-position
from src.State import ButtonStateLookUpTable


class MenuText(Menu):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    def __init__(self):
        self.__current_font: Font = NotAnimated.data["font"]
        self.elements: Tuple[Tuple[Surface]] = ((Surface,),)  # pylint: disable = W,E
        self.internal_states: List[List[Dict[EnumType]]] = [[dict]]
        self.external_states: List[List[Dict[EnumType]]] = [[dict]]
        self.__current_text: str = ""  # pylint: disable=W,E
        self.pos_x: int = 0
        self.pos_y: int = 0

    @property
    def __pos_x(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        return self.pos_x

    @__pos_x.setter
    def set_pos_x(self, new_x: int) -> None:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        self.pos_x = new_x

    @property
    def __pos_y(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        return self.pos_y

    @__pos_y.setter
    def set_pos_y(self, new_y: int) -> None:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        self.pos_y = new_y

    @property
    def mouse_state(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        return self.external_states[0][0]["mouse_state"]

    @mouse_state.setter
    def set_mouse_state(self, state: EnumType):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        self.external_states[0][0]["mouse_state"] = state

    @property
    def current_text(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        return self.__current_text

    @current_text.setter
    def set_text(self, text: str):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        self.__current_text = text

    def relative_pos(self) -> Tuple[int, int]:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        return (self.pos_x, self.pos_y)

    def relative_height(self) -> int:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        if self.elements[0][0]:
            return Surface.get_height(self.elements[0][0])

        raise RuntimeError("Elements are not initiliazed")

    def relative_width(self) -> int:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        if self.elements[0][0]:
            return Surface.get_width(self.elements[0][0])

        raise RuntimeError("Elements are not initiliazed")

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
        """Method for adjust object for internal and external states

        This method has two private method (run_cache, get_color)
        these two method use lru cache to return proper Surface
        object at the end

        NOTE: Check this method for docstrings and structure !!!

        Return:
            Returns Surface object that adjusted based on states
        """

        @lru_cache
        def run_cache(text: str, state: EnumType) -> Tuple[Tuple[Surface]]:
            """Cached pivate method for run()

            Args:
                text (str) : It is caching parameter, simply equals to self.current_text
                punto (int) : It is caching parameter, simply equals to self.current_punto
            Return:
                Returns Tuple in Tuple as ptr Tuple[Tuple[Surface]]
            """
            tmp_color: Tuple[int, int, int] = get_color(state)

            return ((self.__current_font.render(self.current_text, False, tmp_color),),)

        @lru_cache
        def get_color(state: EnumType) -> Tuple[int, int, int]:
            """Returns cached color tuple

            TODO: Adjust colors

            Args:
                state (EnumType) : must be one of ButtonStateLookUpTable values
            Return:
                Returns color as Tuple[int,int,int]
            """
            match state:
                case ButtonStateLookUpTable.CLICKED:
                    return (0, 0, 0)
                case ButtonStateLookUpTable.ON_CLICK:
                    return (181, 181, 181)
                case ButtonStateLookUpTable.NOT_COLLIDE:
                    return (255, 255, 255)
                case _:
                    raise TypeError(
                        f"State must be one of ButtonStateLookUpTable, current {state.__name__}"
                    )

        return run_cache(self.current_text, self.mouse_state)

    def init_external_states(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        self.external_states = [[{}]]

    def init_internal_states(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        self.internal_states = [[{}]]

    def init_elements(self):  # pylint: disable=W
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        self.elements = (
            (self.__current_font.render(self.current_text, False, (255, 255, 255)),),
        )

    def __change_color(self) -> None:  # pylint: disable=W
        raise NotImplementedError

    def update_states(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError
