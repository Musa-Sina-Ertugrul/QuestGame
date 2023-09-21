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
    def create_support_items() -> Tuple[object]:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def create_enemies() -> Tuple[object]:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        def update_enemies() -> Tuple[object]:  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        def create_boss() -> Tuple[object]:  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        def create_mini_boss() -> Tuple[object]:  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        def create_mini_enemy() -> Tuple[object]:  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        raise NotImplementedError

    @staticmethod
    def create_players() -> Tuple[object]:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        def create_elenore() -> Tuple[object]:  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        def create_moonpie() -> Tuple[object]:  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        raise NotImplementedError

    @staticmethod
    def create_loading_menu() -> Tuple[object]:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        def create_loading_menu_bg() -> Tuple[object]:  # pylint: disable=W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        raise NotImplementedError

    @staticmethod
    def create_main_menu() -> Tuple[object]:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        def choose_main_menu_bg() -> Tuple[object]:  # pylint: disable=W,E
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

        raise NotImplementedError

    @staticmethod
    def create_markets() -> Tuple[object]:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        def create_market_bg() -> Tuple[object]:  # pylint: disable=W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        def create_menu_label_market_bg() -> Tuple[object]:  # pylint: disable=W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        def create_gunslinger_jane_market():  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        def create_king_elliot_market():  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        def create_leaf_ranger_galadriel_market():  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        def create_monk_aishi_market():  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        def create_witch_glinda_market():  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        raise NotImplementedError

    @staticmethod
    def create_levels() -> Tuple[object]:
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        def create_cave_level():  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        def create_catacomb_level():  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        raise NotImplementedError

    @staticmethod
    def create_resume_menu() -> Tuple[object]:  # pylint: disable=W,E
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        def create_resume_menu_bg() -> Tuple[object]:  # pylint: disable=W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        raise NotImplementedError

    @staticmethod
    def __create_button():  # pylint: disable = W,E
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        def __create_exit_button():  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        def __create_start_button():  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        def __create_confirm_button():  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        def __create_resume_button():  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        def __create_sound_button():  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        def __create_star_button():  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        def __command_start_button():  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        def __command_star_button():  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        def __command_exit_button():  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        def __command_settings_button():  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        def __command_sound_button():  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        def __command_confirm_button():  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        def __command_display_size_button():  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        def __command_sound_level_button():  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        def __command_sound_button():  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

    raise NotImplementedError

    @staticmethod
    def __create_icon():  # pylint: disable = W,E
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def __create_column():  # pylint: disable = W,E
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def __create_icon_text(icon: EnumType):  # pylint: disable = W,E
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def __create_clock():  # pylint: disable = W,E
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def create_enemy_damage_texts():  # pylint: disable = W,E
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def create_player_texts():  # pylint: disable = W,E
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def __create_health_bar():  # pylint: disable = W,E
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def __create_shield_bar():  # pylint: disable = W,E
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def __create_spell_label():  # pylint: disable = W,E
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def __create_chests() -> Tuple[object]:  # pylint: disable = W,E
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def __create_coin_label() -> Tuple[object]:  # pylint: disable = W,E
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def create_bow() -> Tuple[object]:  # pylint: disable = W,E
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        raise NotImplementedError

    @staticmethod
    def create_bullet():
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        def create_elenore_spell() -> Tuple[object]:  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        def create_bow_line():  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """
            raise NotImplementedError

        raise NotImplementedError

    @staticmethod
    def __command_skills() -> Tuple[object]:  # pylint: disable = W,E
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        # TODO: Give names to skills then update names

        def command_skill_1() -> Tuple[object]:  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        def command_skill_2() -> Tuple[object]:  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        raise NotImplementedError
