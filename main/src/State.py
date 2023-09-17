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
    ON_CLICK : EnumType = 5
    CLICKED : EnumType = 6
    ACTIVE: EnumType = 7
    DEACTIVE: EnumType = 8
    DYING: EnumType = 9
    DEAD: EnumType = 10
    SPAWNING: EnumType = 11
    SCROLL_DOWN: EnumType = 12
    SCROLL_UP : EnumType = 13
    VISIBLE: EnumType = 14
    NOT_VISIBLE: EnumType = 15
