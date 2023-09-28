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

from src.Run import Run

class Gui(Run):
    """sumary_line

    Keyword arguments:

    argument -- description

    Return: return_description
    """

    def __init__(self):

        self.__loading_menu_ptr: Tuple[object] = ((object,),)

        self.__start_menu_ptr: Tuple[object] = ((object,),)

        self.__resume_menu_ptr: Tuple[object] = ((object,),)

        self.__markets_ptr: Tuple[Tuple[object]] = ((object,),)

        self.__levels_ptr: Tuple[object] = ((object,),)

        self.__cv_ptr_tuple: Tuple[Tuple[Condition]] = (
            (Condition() for _ in range(6)),
        )  # pylint: disable=W,E

        self.elements: Tuple[Tuple[object]] = ((object,),)

        self.states: Tuple[Tuple[EnumType]] = ((EnumType,),)

    def run(self):
        """sumary_line

        Keyword arguments:

        argument -- description

        Return: return_description

        TODO: This method will be implemented after states

        """

        if NotImplemented:

            raise NotImplementedError

    @property
    def loading_menu_ptr(self) -> Tuple[object]:
        """sumary_line

        Keyword arguments:

        argument -- description

        Return: return_description
        """

        return self.__loading_menu_ptr

    @property
    def start_menu_ptr(self) -> Tuple[object]:
        """sumary_line

        Keyword arguments:

        argument -- description

        Return: return_description
        """
        return self.__start_menu_ptr

    @property
    def pause_menu_ptr(self) -> Tuple[object]:
        """sumary_line

        Keyword arguments:

        argument -- description

        Return: return_description
        """
        return self.__resume_menu_ptr

    @property
    def shop_menu_ptr(self) -> Tuple[object]:
        """sumary_line

        Keyword arguments:

        argument -- description

        Return: return_description
        """

        return self.__markets_ptr

    @property
    def game_play_ptr(self) -> Tuple[object]:
        """sumary_line

        Keyword arguments:

        argument -- description

        Return: return_description
        """
        return self.__levels_ptr

    @property
    def loading_menu_flag(self, is_relased: bool) -> NoReturn:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        if is_relased:

            self.__cv_ptr_tuple[0][0].notify()
        else:

            self.__cv_ptr_tuple[0][0].wait()

    @property
    def start_menu_flag(self, is_relased: bool) -> NoReturn:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        if is_relased:

            self.__cv_ptr_tuple[0][1].notify()
        else:

            self.__cv_ptr_tuple[0][1].wait()

    @property
    def pause_menu_flag(self, is_relased: bool) -> NoReturn:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        if is_relased:

            self.__cv_ptr_tuple[0][2].notify()
        else:

            self.__cv_ptr_tuple[0][2].wait()

    @property
    def shop_menu_flag(self, is_relased: bool) -> NoReturn:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        if is_relased:

            self.__cv_ptr_tuple[0][3].notify()
        else:

            self.__cv_ptr_tuple[0][3].wait()

    @property
    def npc_menu_flag(self, is_relased: bool) -> NoReturn:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        if is_relased:

            self.__cv_ptr_tuple[0][4].notify()
        else:

            self.__cv_ptr_tuple[0][4].wait()

    @property
    def game_play_flag(self, is_relased: bool) -> NoReturn:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
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
