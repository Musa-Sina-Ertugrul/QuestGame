"""sumary_line

Keyword arguments:
argument -- description
Return: return_description

TODO: Update Docstrings

"""
from typing import Tuple
from .Run import Run
from .utils.utils import (
    singelton,
)  # pylint: disable = import-error, no-name-in-module,wrong-import-order,wrong-import-position
from .factory.Factory import Factory

# NOTE: Don't try creating software object it is singleton


@singelton
class Software(Run):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    # TODO: Give dissicion about init_observers can be in Factory

    def __init__(self):
        # TODO: Implement
        # self.__observers_ptr : Tuple[Tuple[Dict]] = self.__init_observers() # pylint: disable= W,E
        # self.__objects_ptr : Tuple[Tuple[Dict]] = self.__init_objects() # pylint: disable= W,E
        self.__guis_ptr: Tuple[
            Tuple[object]
        ] = self.__init_guis()  # pylint: disable= W,E

    def run(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    def __init_observers(self):  # pylint: disable= W,E
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    def __init_objects(self):  # pylint: disable= W,E
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    def __init_guis(self) -> Tuple[Tuple[object]]:  # pylint: disable= W,E
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        # TODO: Implement
        # raise NotImplementedError
        return Factory.create_guis()
