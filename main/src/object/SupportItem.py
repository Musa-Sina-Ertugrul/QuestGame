"""sumary_line

Keyword arguments:
argument -- description
Return: return_description

TODO: Update Docstrings

"""
from abc import abstractmethod, ABC
from typing import Tuple, NoReturn
from enum import EnumType
from ..Object import Object  # pylint: disable = import-error, no-name-in-module,wrong-import-order,wrong-import-position


class SupportItem(Object, ABC):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    def __init__(self):
        Object.__init__(self)
        Object.elements: Tuple[
            Tuple[object]
        ] = self.init_elements()  # pylint: disable = W,E
        Object.states: Tuple[
            Tuple[EnumType]
        ] = self.init_states()  # pylint: disable = W,E

    @abstractmethod
    def choose_random(self):
        """sumary_line
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError


    @abstractmethod
    def run(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    @abstractmethod
    def notify_states(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    @abstractmethod
    def init_elements(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    @abstractmethod
    def init_states(self):
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
    def update_states(self) -> NoReturn:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    @abstractmethod
    def apply_effects(self):
        """sumary_line
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    @abstractmethod
    def multiplate_support_item(self):
        """sumary_line
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    @abstractmethod
    def init_command(self):
        """sumary_line
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError
