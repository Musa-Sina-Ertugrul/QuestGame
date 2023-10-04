"""sumary_line

Keyword arguments:
argument -- description
Return: return_description

TODO: Update Docstrings
TODO: Add more table and states

"""

from enum import Enum, EnumType


class StateLookUpTable(Enum):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description

    TODO: That lookup table will be deleted and new lookup tables will be created

    """

    NULL: EnumType = 0
    LOADING: EnumType = 1
    START: EnumType = 2
    SHOP: EnumType = 3
    OPTIONS: EnumType = 4
    ON_CLICK: EnumType = 5
    CLICKED: EnumType = 6
    ACTIVE: EnumType = 7
    DEACTIVE: EnumType = 8
    DYING: EnumType = 9
    DEAD: EnumType = 10
    SPAWNING: EnumType = 11
    SCROLL_DOWN: EnumType = 12
    SCROLL_UP: EnumType = 13
    VISIBLE: EnumType = 14
    NOT_VISIBLE: EnumType = 15


class PlayerLookUpTable(Enum):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    NULL: EnumType = 0


class EnemyLookUpTable(Enum):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    NULL: EnumType = 0


class ResumeMenuLookUpTable(Enum):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    NULL: EnumType = 0


class MainMenuLookUpTable(Enum):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    NULL: EnumType = 0


class LoadingMenuLookUpTable(Enum):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    NULL: EnumType = 0


class SpellLookUpTable(Enum):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    NULL: EnumType = 0


class MarketLookUpTable(Enum):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    NULL: EnumType = 0


class MenuTextLookUpTable(Enum):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    NULL: EnumType = 0


class ButtonLookUpTable(Enum):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description

    TODO: Add more button

    """

    NULL: EnumType = 0
    EXIT_BUTTON: EnumType = 1
    START_BUTTON: EnumType = 2
    CONFIRM_BUTTON: EnumType = 3
    RESUME_BUTTON: EnumType = 4
    SOUND_ON_OFF_BUTTON: EnumType = 5
    STAR_BUTTON: EnumType = 6
    SOUND_LEVEL_BUTTON: EnumType = 7


class ButtonStateLookUpTable(Enum):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    NULL: EnumType = 0
    CLICKED: EnumType = 1
    ON_CLICK: EnumType = 2
    NOT_COLLIDE: EnumType = 3
    VISIBLE: EnumType = 4
    NOT_VISIBLE: EnumType = 5
    SOUND_UP: EnumType = 6
    SOUND_DOWN: EnumType = 7


class MenuLabelStateLookUpTable(Enum):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    NULL: EnumType = 0
    COLLIDE: EnumType = 1
    NOT_COLLIDE: EnumType = 2
    VISIBLE: EnumType = 3
    NOT_VISIBLE: EnumType = 4
