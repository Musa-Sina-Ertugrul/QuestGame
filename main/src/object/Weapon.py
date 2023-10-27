"""sumary_line

Keyword arguments:
argument -- description
Return: return_description

TODO: Update Docstrings

"""

from typing import  Tuple, Dict
from ..Object import Object  # pylint: disable = W,E
from ..Run import Run


class Weapon(Object, Run):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    def __init__(self):
        Object.__init__(self)
        Object.elements = ((object,),)
        Object.internal_states: Tuple[Tuple[Dict]] = ((dict,),)
        Object.external_states: Tuple[Tuple[Dict]] = ((dict,),)
        self.pos_x: int = 0
        self.pos_y: int = 0
        self.tetha: float = 0.0

    @property
    def pos_x(self) -> int:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        return self.pos_x

    @pos_x
    def set_pos_x(self, new_x: int) -> None:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        self.pos_x = new_x

    @property
    def pos_y(self) -> int:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        return self.pos_y

    @pos_y
    def set_pos_y(self, new_y: int) -> None:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        self.pos_y = new_y

    def fire(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    @property
    def tetha(self) -> int:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        return self.pos_x

    @pos_x
    def set_tetha(self, new_tetha: float) -> None:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        if new_tetha > 360.0 or new_tetha < 0:
            raise ValueError
        self.tetha = new_tetha

    def calculate_tetha(
        self, vector_1: object, vector_2: object
    ) -> None:  # pylint: disable = W,E
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

    def apply_effects(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError
