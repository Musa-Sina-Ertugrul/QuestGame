"""sumary_line

Keyword arguments:
argument -- description
Return: return_description

TODO: Update Docstrings

"""

from typing import NoReturn, Tuple
from ..Market import Market

class GunSlingerJane(Market):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    def __init__(self):
        super().__init__()
        super.elements = self._init_market()
        self.items: Tuple[Tuple[int]] = [[]]  # TODO: Hardcode items

    def buy_level(self, skill: int):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    def reset_levels(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    def relative_pos(self) -> Tuple[int, int]:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    def relative_height(self) -> int:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    def relative_width(self) -> int:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    def update_elements(self) -> NoReturn:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    def notify_states(self) -> NoReturn:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    def current_pos(self) -> Tuple[int, int]:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        return (self._x, self._y)

    def run(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    def update_skill(self):
        """sumary_line
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError
