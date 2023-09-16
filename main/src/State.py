"""sumary_line

Keyword arguments:
argument -- description
Return: return_description

TODO: Update Docstrings

"""

from enum import Enum, EnumType


class StateLookUpTable(Enum):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description

    TODO: Add more state

    """

    NULL: EnumType = 0
    LOADING: EnumType = 1
    START: EnumType = 2
    SHOP: EnumType = 3
    OPTIONS: EnumType = 4
