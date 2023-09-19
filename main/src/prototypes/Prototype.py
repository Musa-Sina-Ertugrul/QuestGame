"""sumary_line

Keyword arguments:
argument -- description
Return: return_description

TODO: Update Docstrings

"""
from typing import Dict, Tuple
from ..factory.Factory import Factory


class Prototype:
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    data: Dict[str, Tuple[object]] = {}

    data["loading_menu"] = Factory.create_loading_menu()
    data["start_menu"] = Factory.create_start_menu()
    data["pause_menu"] = Factory.create_resume_menu()
    data["shop_menu"] = Factory.create_market_menu()
    data["game_play"] = Factory.create_game_play()

    @staticmethod
    @property.getter
    def get_loading_menu() -> Tuple[object]:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        return (Prototype.data["start_menu"],)

    @staticmethod
    @property.getter
    def get_start_menu() -> Tuple[object]:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        return (Prototype.data["start_menu"],)

    @staticmethod
    @property.getter
    def get_resume_menu() -> Tuple[object]:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        return (Prototype.data["pause_menu"],)

    @staticmethod
    @property.getter
    def get_market_menu() -> Tuple[object]:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        return (Prototype.data["pause_menu"],)

    @staticmethod
    @property.getter
    def get_npc_menu() -> Tuple[object]:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        return (Prototype.data["npc_menu"],)

    @staticmethod
    @property.getter
    def get_game_play() -> Tuple[object]:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        return (Prototype.data["game_play"],)
