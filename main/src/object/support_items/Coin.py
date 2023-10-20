"""sumary_line

Keyword arguments:
argument -- description
Return: return_description

TODO: Update Docstrings

"""
from typing import Tuple, Dict
from ..SupportItem import (
    SupportItem,
)  # pylint: disable = import-error, no-name-in-module,wrong-import-order,wrong-import-position


class Coin(SupportItem):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    def __init__(self):
        super().__init__(self)  # pylint: disable = W,E
        super.elements: Tuple[Tuple[object]] = ((object,),)  # pylint: disable = W,E
        super.internal_states: Tuple[Tuple[Dict]] = ((dict,),)
        super.external_states: Tuple[Tuple[Dict]] = ((dict,),)

    def flip_coin(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    def choose_random(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

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

    def update_elements(self) -> None:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    def update_states(self) -> None:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    def apply_effects(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    def multiplate_support_item(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    def init_command(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError
