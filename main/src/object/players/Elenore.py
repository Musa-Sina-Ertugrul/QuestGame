"""sumary_line

Keyword arguments:
argument -- description
Return: return_description

TODO: Update Docstrings

"""
from sys import path

path.append("main/src/utils")

from typing import (  # pylint: disable = import-error, no-name-in-module,wrong-import-order,wrong-import-position
    Tuple,  # pylint: disable = import-error, no-name-in-module,wrong-import-order,wrong-import-position
    Dict,  # pylint: disable = import-error, no-name-in-module,wrong-import-order,wrong-import-position
)  # pylint: disable = import-error, no-name-in-module,wrong-import-order,wrong-import-position
from utils import (  # pylint: disable = import-error, no-name-in-module,wrong-import-order,wrong-import-position
    singelton,  # pylint: disable = import-error, no-name-in-module,wrong-import-order,wrong-import-position
)  # pylint: disable = import-error, no-name-in-module,wrong-import-order,wrong-import-position
from ..Player import (  # pylint: disable = import-error, no-name-in-module,wrong-import-order,wrong-import-position
    Player,  # pylint: disable = import-error, no-name-in-module,wrong-import-order,wrong-import-position
)  # pylint: disable = import-error, no-name-in-module,wrong-import-order,wrong-import-position


@singelton
class MoonPie(Player):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    def __init__(self):
        super().__init__(self)  # pylint: disable = W,E
        self.elements: Tuple[Tuple[object]] = ((object,),)  # pylint: disable = W,E
        self.internal_states: Tuple[Tuple[Dict]] = ((dict,),)
        self.external_states: Tuple[Tuple[Dict]] = ((dict,),)

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

    def death(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    def take_hit(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    def move(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    def fire(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    def reload(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError
