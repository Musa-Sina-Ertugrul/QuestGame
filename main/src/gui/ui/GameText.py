"""sumary_line

Keyword arguments:
argument -- description
Return: return_description

TODO: Update Docstrings

"""
from sys import path
from typing import Tuple, NoReturn, Dict
from copy import copy
from pygame.font import Font

path.append("main/src/flyweights")
path.append("main/src/")

from not_animated import (  # pylint: disable=W,E,import-error,wrong-import-position
    NotAnimated,
)
from State import (  # pylint: disable=W,E,import-error,wrong-import-position
    StateLookUpTable,
)
from ..Game import Game  # pylint: disable=W,E,import-error,wrong-import-position


class GameText(Game):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    def __init__(self):
        super().__init__(self)  # pylint: disable=W,E
        self.__current_font: Tuple[Font] = (  # pylint: disable=W,E
            copy(NotAnimated.data["font"]),  # pylint: disable=W,E
        )
        super.elements: Tuple[
            Tuple[object]
        ] = ((object,),) # pylint: disable = W,E
        super.internal_states: Tuple[Tuple[Dict]] = ((dict,),)
        super.external_states: Tuple[Tuple[Dict]] = ((dict,),)
        self.__current_text: str = ""  # pylint: disable=W,E
        self.__current_punto: int = 0  # pylint: disable=W,E

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

    @property
    def current_punto(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        return self.__current_text

    @current_text.setter
    def set_punto(self, punto: int):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        self.__current_punto = punto  # pylint: disable=W,E

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

    def init_elements(self) -> Tuple[Tuple[Font]]:  # pylint: disable=W
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
