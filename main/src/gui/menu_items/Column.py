"""sumary_line

Keyword arguments:
argument -- description
Return: return_description

TODO: Update Docstrings

"""
from typing import Tuple, None, Dict
from ..Menu import Menu


class Column(Menu):

    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    def __init__(self):
        super().__init__(self)  # pylint: disable=E
        super.elements: Tuple[Tuple[object]] = ((object,),)  # pylint: disable = W,E
        super.internal_states: Tuple[Tuple[Dict]] = ((dict,),)
        super.external_states: Tuple[Tuple[Dict]] = ((dict,),)

    @property
    def pos_x(self) -> int:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        return super().pos_x

    @pos_x.setter
    def pos_x(self, new_x: int) -> None:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        super().pos_x = new_x

    @property
    def pos_y(self) -> int:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        return super().pos_y

    @pos_y.setter
    def pos_y(self, new_y: int) -> None:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        super().pos_y = new_y

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

    def update_elements(self) -> None:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    def notify_states(self) -> None:
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
        return (self.pos_x, self.pos_y)

    def run(self):
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

    def init_elements(  # pylint: disable=W
        self, item_list: Tuple[Tuple[object]]
    ) -> Tuple[Tuple[object]]:  # pylint: disable=W
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    def update_states(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError
