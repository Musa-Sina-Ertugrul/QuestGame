"""sumary_line

Keyword arguments:
argument -- description
Return: return_description

TODO: object assigments will change after implementations
TODO: Update Docstrings
"""
from typing import List, NoReturn
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
        self.__loading_menu_ptr: List[object] = Prototype.get_loading_menu()
        self.__start_menu_ptr: List[object] = Prototype.get_start_menu()
        self.__pause_menu_ptr: List[object] = Prototype.get_pause_menu()
        self.__shop_menu_ptr: List[object] = Prototype.get_shop_menu()
        self.__npc_menu_ptr: List[object] = Prototype.get_npc_menu()
        self.__game_play_ptr: List[object] = Prototype.get_game_play()
        self.__cv_ptr_list: List[Condition] = []
        self.__cv_ptr_list = [Condition() for _ in range(6)]
        self._width = 1920
        self._height = 1080

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
    def loading_menu_ptr(self) -> List[object]:
        return self.__loading_menu_ptr

    @property.getter
    def start_menu_ptr(self) -> List[object]:
        return self.__start_menu_ptr

    @property.getter
    def pause_menu_ptr(self) -> List[object]:
        return self.__pause_menu_ptr

    @property.getter
    def shop_menu_ptr(self) -> List[object]:
        return self.__shop_menu_ptr

    @property.getter
    def npc_menu_ptr(self) -> List[object]:
        return self.__npc_menu_ptr

    @property.getter
    def game_play_ptr(self) -> List[object]:
        return self.__game_play_ptr

    @property.setter
    def loading_menu_flag(self, is_relased: bool) -> NoReturn:
        if is_relased:
            self.__cv_ptr_list[0].notify()
        else:
            self.__cv_ptr_list[0].wait()

    @property.setter
    def start_menu_flag(self, is_relased: bool) -> NoReturn:
        if is_relased:
            self.__cv_ptr_list[1].notify()
        else:
            self.__cv_ptr_list[1].wait()

    @property.setter
    def pause_menu_flag(self, is_relased: bool) -> NoReturn:
        if is_relased:
            self.__cv_ptr_list[2].notify()
        else:
            self.__cv_ptr_list[2].wait()

    @property.setter
    def shop_menu_flag(self, is_relased: bool) -> NoReturn:
        if is_relased:
            self.__cv_ptr_list[3].notify()
        else:
            self.__cv_ptr_list[3].wait()

    @property.setter
    def npc_menu_flag(self, is_relased: bool) -> NoReturn:
        if is_relased:
            self.__cv_ptr_list[4].notify()
        else:
            self.__cv_ptr_list[4].wait()

    @property.setter
    def game_play_flag(self, is_relased: bool) -> NoReturn:
        if is_relased:
            self.__cv_ptr_list[5].notify()
        else:
            self.__cv_ptr_list[5].wait()
