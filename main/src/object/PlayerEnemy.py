"""sumary_line

Keyword arguments:
argument -- description
Return: return_description

TODO: Update Docstrings

"""

from abc import ABCMeta, abstractmethod


class PlayerWeapon(metaclass=ABCMeta):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, "death") and callable(subclass.death) or NotImplemented,
            hasattr(subclass, "take_hit")
            and callable(subclass.take_hit)
            or NotImplemented,
            hasattr(subclass, "move") and callable(subclass.move) or NotImplemented,
        )

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
