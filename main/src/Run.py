"""
Run class is an interface

This insterface has been used by states,
observers, gui and object
"""
from abc import ABCMeta, abstractmethod


class Run(metaclass=ABCMeta):

    """
    Run class is an interface and facade
    """

    @classmethod
    def __subclasshook__(cls, subclass):
        return hasattr(subclass, "run") and callable(subclass.run) or NotImplemented

    @abstractmethod
    def run(self):
        """
        Command function to adjust final methods
        """
        raise NotImplementedError
