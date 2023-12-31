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
            hasattr(subclass, "reload") and callable(subclass.reload) or NotImplemented,
            hasattr(subclass, "fire") and callable(subclass.fire) or NotImplemented,
        )

    @abstractmethod
    def reload(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    @abstractmethod
    def fire(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError
