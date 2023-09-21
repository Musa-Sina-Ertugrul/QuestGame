"""sumary_line

Keyword arguments:

argument -- description

Return: return_description

TODO: object assigments will change after implementations

TODO: Update Docstrings
"""

from typing import Tuple, NoReturn

from enum import EnumType

from multiprocessing import Condition

from .Run import Run

from .prototypes.Prototype import Prototype


class Gui(Run):
    """sumary_line

    Keyword arguments:

    argument -- description

    Return: return_description
    """

    def __init__(self):

        self.__loading_menu_ptr: Tuple[object] = Prototype.get_loading_menu()

        self.__start_menu_ptr: Tuple[object] = Prototype.get_start_menu()

        self.__resume_menu_ptr: Tuple[object] = Prototype.get_resume_menu()

        self.__markets_ptr: Tuple[Tuple[object]] = Prototype.get_markets()

        self.__levels_ptr: Tuple[object] = Prototype.get_levels()

        self.__cv_ptr_tuple: Tuple[Tuple[Condition]] = (
            (Condition() for _ in range(6)),
        )  # pylint: disable=W,E

        self.elements: Tuple[Tuple[object]] = self.init_elements()

        self.states: Tuple[Tuple[EnumType]] = self.init_states()

    def run(self):
        """sumary_line

        Keyword arguments:

        argument -- description

        Return: return_description

        TODO: This method will be implemented after states

        """

        if NotImplemented:

            raise NotImplementedError

    @property.getter
    def loading_menu_ptr(self) -> Tuple[object]:
        """sumary_line

        Keyword arguments:

        argument -- description

        Return: return_description
        """

        return self.__loading_menu_ptr

    @property.getter
    def start_menu_ptr(self) -> Tuple[object]:
        """sumary_line

        Keyword arguments:

        argument -- description

        Return: return_description
        """
        return self.__start_menu_ptr

    @property.getter
    def pause_menu_ptr(self) -> Tuple[object]:
        """sumary_line

        Keyword arguments:

        argument -- description

        Return: return_description
        """
        return self.__resume_menu_ptr

    @property.getter
    def shop_menu_ptr(self) -> Tuple[object]:
        """sumary_line

        Keyword arguments:

        argument -- description

        Return: return_description
        """

        return self.__markets_ptr

    @property.getter
    def game_play_ptr(self) -> Tuple[object]:
        """sumary_line

        Keyword arguments:

        argument -- description

        Return: return_description
        """
        return self.__levels_ptr

    @property.setter
    def loading_menu_flag(self, is_relased: bool) -> NoReturn:
        if is_relased:

            self.__cv_ptr_tuple[0][0].notify()
        else:

            self.__cv_ptr_tuple[0][0].wait()

    @property.setter
    def start_menu_flag(self, is_relased: bool) -> NoReturn:
        if is_relased:

            self.__cv_ptr_tuple[0][1].notify()
        else:

            self.__cv_ptr_tuple[0][1].wait()

    @property.setter
    def pause_menu_flag(self, is_relased: bool) -> NoReturn:
        if is_relased:

            self.__cv_ptr_tuple[0][2].notify()
        else:

            self.__cv_ptr_tuple[0][2].wait()

    @property.setter
    def shop_menu_flag(self, is_relased: bool) -> NoReturn:
        if is_relased:

            self.__cv_ptr_tuple[0][3].notify()
        else:

            self.__cv_ptr_tuple[0][3].wait()

    @property.setter
    def npc_menu_flag(self, is_relased: bool) -> NoReturn:
        if is_relased:

            self.__cv_ptr_tuple[0][4].notify()
        else:

            self.__cv_ptr_tuple[0][4].wait()

    @property.setter
    def game_play_flag(self, is_relased: bool) -> NoReturn:
        if is_relased:

            self.__cv_ptr_tuple[0][5].notify()
        else:

            self.__cv_ptr_tuple[0][5].wait()

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

    def update_elements(self) -> NoReturn:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    def update_states(self) -> NoReturn:
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
