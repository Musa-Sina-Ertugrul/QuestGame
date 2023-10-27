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
            hasattr(subclass, "init_external_states")
            and callable(subclass.init_states)
            or NotImplemented,
            hasattr(subclass, "init_internal_states")
            and callable(subclass.init_states)
            or NotImplemented,
            hasattr(subclass, "init_elements")
            and callable(subclass.init_elements)
            or NotImplemented,
            hasattr(subclass, "update_elements")
            and callable(subclass.update_elements)
            or NotImplemented,
            hasattr(subclass, "update_states")
            and callable(subclass.update_states)
            or NotImplemented,
            hasattr(subclass, "notify_states")
            and callable(subclass.notify_states)
            or NotImplemented,
        )

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
    def init_elements(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    @abstractmethod
    def update_elements(self) -> None:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    @abstractmethod
    def update_states(self) -> None:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    @abstractmethod
    def notify_states(self) -> None:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError
