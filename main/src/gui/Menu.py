"""sumary_line

Keyword arguments:
argument -- description
Return: return_description

TODO: Update Docstrings

"""
from enum import EnumType
from abc import ABC, abstractmethod
from typing import List, Tuple, NoReturn
from ..Gui import Gui  # pylint: disable=E
from ..State import (   # pylint: disable=W # When this line has been used delete pylint hint
    StateLookUpTable,   # pylint: disable=W
) # pylint: disable=W

class Menu(Gui, ABC):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    def __init__(self):
        self._elements: List[List[object]] = [[]]
        self._connected_states: List[List[EnumType]] = [[]]
        self._x: int = 0
        self._y: int = 0
        self._width: int = self._relative_width()
        self._height: int = self._relative_height()

    @abstractmethod
    def _relative_pos(self) -> Tuple[int, int]:
        raise NotImplementedError

    @abstractmethod
    def _relative_height(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def _relative_width(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def _update_elements(self) -> NoReturn:
        raise NotImplementedError

    @abstractmethod
    def _notify_states(self) -> NoReturn:
        raise NotImplementedError

    def run(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError
