"""sumary_line

Keyword arguments:
argument -- description
Return: return_description

TODO: Update Docstrings

"""

from typing import NoReturn, Tuple, Dict
from ..Weapon import Weapon


class ElenoreSpell(Weapon):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    def __init__(self):
        super().__init__(self)  # pylint: disable = W,E
        super.elements = ((object,),)
        super.internal_states: Tuple[Tuple[Dict]] = ((dict,),)
        super.external_states: Tuple[Tuple[Dict]] = ((dict,),)
        super.pos_x: int = 0
        super.pos_y: int = 0
        super.tetha: float = 0.0

    @property
    def pos_x(self) -> int:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        return self.pos_x

    @pos_x
    def set_pos_x(self, new_x: int) -> NoReturn:
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
    def set_pos_y(self, new_y: int) -> NoReturn:
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
    def set_tetha(self, new_tetha: float) -> NoReturn:
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
    ) -> NoReturn:  # pylint: disable = W,E
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
