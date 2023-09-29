"""sumary_line

Keyword arguments:
argument -- description
Return: return_description

TODO: Update Docstrings

"""
from abc import ABC, abstractmethod
from typing import Tuple, Dict
from ..Object import Object  # pylint: disable = import-error, no-name-in-module
from .PlayerEnemy import (  # pylint: disable = import-error, no-name-in-module
    PlayerEnemy,  # pylint: disable = import-error, no-name-in-module
)  # pylint: disable = import-error, no-name-in-module


class Enemy(Object, PlayerEnemy, ABC):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    def __init__(self):
        Object.__init__(self)  # pylint: disable = W,E
        self.elements: Tuple[
            Tuple[object]
        ] = ((object,),)  # pylint: disable = W,E
        Object.internal_states: Tuple[Tuple[Dict]] = ((dict,),)
        Object.external_states: Tuple[Tuple[Dict]] = ((dict,),)

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
    def init_external_states(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    @abstractmethod
    def init_internal_states(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    @abstractmethod
    def death(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    @abstractmethod
    def take_hit(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    @abstractmethod
    def move(self):
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
