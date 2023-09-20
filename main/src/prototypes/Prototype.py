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
    data["resume_menu"] = Factory.create_resume_menu()
    data["markets"] = Factory.create_markets()
    data["levels"] = Factory.create_levels()

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

        return (Prototype.data["resume_menu"],)

    @staticmethod
    @property.getter
    def get_markets() -> Tuple[object]:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        return (Prototype.data["markets"],)

    @staticmethod
    @property.getter
    def get_levels() -> Tuple[object]:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        return (Prototype.data["levels"],)
