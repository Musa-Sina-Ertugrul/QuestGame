"""sumary_line

Keyword arguments:
argument -- description
Return: return_description

TODO: Update Docstrings

"""
from sys import path

path.append("main/src/flyweights")

from copy import copy #pylint: disable=import-error,wrong-import-position
from typing import Tuple, NoReturn #pylint: disable=import-error,wrong-import-position
from animated import Animated #pylint: disable=import-error,wrong-import-position
from ..MenuButton import MenuButton #pylint: disable=import-error,wrong-import-position

class ConfirmButton(MenuButton):
    """sumary_line
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    def __init__(self):
        super().__init__(self) #pylint: disable=W,E
        super.current_button_img = 0
        super.button_imgs = (copy(Animated.data["confirm_button"])) #pylint: disable=W,E,superfluous-parens
        super.elements = self.init_elements()
        super.states = self.init_states()

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
        if NotImplemented:
            raise NotImplementedError
        return (self.pos_x, self.pos_y)

    def run(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    def init_states(self):
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
