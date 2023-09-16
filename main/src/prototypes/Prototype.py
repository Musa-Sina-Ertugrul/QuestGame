"""sumary_line

Keyword arguments:
argument -- description
Return: return_description

TODO: Update Docstrings

"""
from typing import Dict, List
from ..factory.Factory import Factory


class Prototype:
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    data: Dict[str, List[object]] = {}

    data["loading_menu"] = Factory.create_loading_menu()
    data["start_menu"] = Factory.create_start_menu()
    data["pause_menu"] = Factory.create_pause_menu()
    data["shop_menu"] = Factory.create_shop_menu()
    data["npc_menu"] = Factory.create_npc_menu()
    data["game_play"] = Factory.create_game_play()

    @staticmethod
    @property.getter
    def get_loading_menu() -> List[object]:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        return Prototype.data["start_menu"]

    @staticmethod
    @property.getter
    def get_start_menu() -> List[object]:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        return Prototype.data["start_menu"]

    @staticmethod
    @property.getter
    def get_pause_menu() -> List[object]:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        return Prototype.data["pause_menu"]

    @staticmethod
    @property.getter
    def get_shop_menu() -> List[object]:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        return Prototype.data["pause_menu"]

    @staticmethod
    @property.getter
    def get_npc_menu() -> List[object]:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        return Prototype.data["npc_menu"]

    @staticmethod
    @property.getter
    def get_game_play() -> List[object]:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        return Prototype.data["game_play"]
