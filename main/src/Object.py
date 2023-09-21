"""sumary_line

Keyword arguments:
argument -- description
Return: return_description

TODO: Update Docstrings

"""
from typing import Tuple, NoReturn
from enum import EnumType
from .prototypes.Prototype import Prototype
from .Run import Run
from .ObjectGui import (
    ObjectGui,
)  # pylint: disable = import-error, no-name-in-module,wrong-import-order,wrong-import-position


class Object(Run, ObjectGui):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    def __init__(self):
        self.__players_ptr: Tuple[  # pylint: disable = W,E
            Tuple[object]
        ] = Prototype.get_players()  # pylint: disable = W,E
        self.__enemies_ptr: Tuple[  # pylint: disable = W,E
            Tuple[object]
        ] = Prototype.get_enemies()  # pylint: disable = W,E
        self.__support_items_ptr: Tuple[  # pylint: disable = W,E
            Tuple[object]
        ] = Prototype.get_support_items()  # pylint: disable = W,E
        self.elements: Tuple[
            Tuple[object]
        ] = self.init_elements()  # pylint: disable = W,E
        self.states: Tuple[
            Tuple[EnumType]
        ] = self.init_states()  # pylint: disable = W,E

    def run(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    def notify_states(self):
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

    def init_states(self):
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

    def update_states(self) -> NoReturn:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError
