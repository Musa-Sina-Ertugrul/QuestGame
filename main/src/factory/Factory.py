"""sumary_line

Keyword arguments:
argument -- description
Return: return_description

TODO: When implementations are done functions will be filled and object typing will be changed
TODO: Update Docstrings
"""
from typing import Tuple
from numpy import random

class Factory:
    """ "sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    @staticmethod
    def create_loading_menu() -> Tuple[object]:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def create_start_menu() -> Tuple[object]:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def create_markets() -> Tuple[object]:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def create_levels() -> Tuple[object]:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def __choose_main_menu_bg() -> Tuple[object]: # pylint: disable=W,E
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        return (
            NotAnimated.data["bgs_main_menu"][  # pylint: disable=W,E
                int(random.uniform(low=0.0, high=4.999))
            ],  # TODO: These img file has many space determine when they will be called (runtime, compile time) # pylint: disable=W,E
        )

    @staticmethod
    def __create_loading_menu_bg() -> Tuple[object]:  # pylint: disable=W,E
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def __create_market_bg() -> Tuple[object]:  # pylint: disable=W,E
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def create_resume_menu() -> Tuple[object]:  # pylint: disable=W,E
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def __create_resume_menu_bg() -> Tuple[object]:  # pylint: disable=W,E
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def __create_menu_label_market_bg() -> Tuple[object]:  # pylint: disable=W,E
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def __crate_gunslinger_jane_market():  # pylint: disable = W,E
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def __crate_king_elliot_market():  # pylint: disable = W,E
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def __crate_leaf_ranger_galadriel_market():  # pylint: disable = W,E
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def __crate_monk_aishi_market():  # pylint: disable = W,E
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def __crate_witch_glinda_market():  # pylint: disable = W,E
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def __crate_exit_button():  # pylint: disable = W,E
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def __crate_start_button():  # pylint: disable = W,E
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def __crate_confirm_button():  # pylint: disable = W,E
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def __crate_resume_button():  # pylint: disable = W,E
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def __crate_sound_button():  # pylint: disable = W,E
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def __crate_start_button():  # pylint: disable = W,E
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def __crate_star_button():  # pylint: disable = W,E
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def __create_icon(): # pylint: disable = W,E
        """sumary_line
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def __create_column(): # pylint: disable = W,E
        """sumary_line
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def __create_icon_text(icon: EnumType): # pylint: disable = W,E
        """sumary_line
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def __create_cave_level(): # pylint: disable = W,E
        """sumary_line
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def __create_catacomb_level(): # pylint: disable = W,E
        """sumary_line
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def __create_cave_level(): # pylint: disable = W,E
        """sumary_line
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def __create_clock(): # pylint: disable = W,E
        """sumary_line
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def __create_enemy_damage_texts(): # pylint: disable = W,E
        """sumary_line
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def __command_start_button(): # pylint: disable = W,E
        """sumary_line
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def __command_star_button(): # pylint: disable = W,E
        """sumary_line
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def __command_exit_button(): # pylint: disable = W,E
        """sumary_line
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def __command_settings_button(): # pylint: disable = W,E
        """sumary_line
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def __command_sound_button(): # pylint: disable = W,E
        """sumary_line
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def __command_confirm_button(): # pylint: disable = W,E
        """sumary_line
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def __command_display_size_button(): # pylint: disable = W,E
        """sumary_line
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def __command_sound_level_button(): # pylint: disable = W,E
        """sumary_line
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def __command_sound_button(): # pylint: disable = W,E
        """sumary_line
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def __create_player_texts(): # pylint: disable = W,E
        """sumary_line
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def __create_health_bar(): # pylint: disable = W,E
        """sumary_line
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def __create_shield_bar(): # pylint: disable = W,E
        """sumary_line
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def __create_spell_label(): # pylint: disable = W,E
        """sumary_line
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError