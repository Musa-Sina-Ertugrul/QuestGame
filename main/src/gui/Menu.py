"""sumary_line

Keyword arguments:
argument -- description
Return: return_description

TODO: Update Docstrings

"""
from enum import EnumType
from abc import ABC, abstractmethod
from typing import Tuple, NoReturn
from ..Gui import Gui  # pylint: disable=E
from ..State import (  # pylint: disable=W # When this line has been used delete pylint hint
    StateLookUpTable,  # pylint: disable=W
)  # pylint: disable=W


class Menu(Gui, ABC):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    def __init__(self):
        super().__init__(self)
        self.elements: Tuple[Tuple[object]] = [[]]
        self.states: Tuple[Tuple[EnumType]] = [[]]
        self.pos_x: int = 0
        self.pos_y: int = 0
        self.width: int = self._relative_width()
        self.height: int = self._relative_height()

    @abstractmethod
    def relative_pos(self) -> Tuple[int, int]:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @abstractmethod
    def relative_height(self) -> int:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    @abstractmethod
    def relative_width(self) -> int:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    @abstractmethod
    def update_elements(self) -> NoReturn:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    @abstractmethod
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
        return (self.pos_x, self.pos_y)

    def run(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    def init_states(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    def init_elements(self):
        """sumary_line
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError
