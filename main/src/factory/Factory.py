"""sumary_line

Keyword arguments:
argument -- description
Return: return_description

TODO: When implementations are done functions will be filled and object typing will be changed
TODO: Update Docstrings
"""
from enum import EnumType
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

        from src.gui.menu_items.MenuTemplate import ( # pylint: disable=W,E, import-error, import-outside-toplevel
            MenuTemplate, # pylint: disable=W,E, import-error, import-outside-toplevel
        )  # pylint: disable=W,E, import-error, import-outside-toplevel

        return MenuTemplate()

    @staticmethod
    def create_guis():
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        from sys import path # pylint: disable=W,E, import-error, import-outside-toplevel

        path.append("main/src/")
        from Gui import Gui # pylint: disable=W,E, import-error, import-outside-toplevel

        return ((Gui(),),)

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
    def __create_button(button_no: EnumType):  # pylint: disable = W,E
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description

        TODO: Add more text button

        """

        from src.State import ButtonLookUpTable # pylint: disable=W,E, import-error, import-outside-toplevel

        def create_text_button(button_no: EnumType):
            """sumary_line
            
            Keyword arguments:
            argument -- description
            Return: return_description

            TODO: Add more button

            """

            from src.gui.menu_items.MenuText import MenuText # pylint: disable=W,E, import-error, import-outside-toplevel

            def create_sound_level_button() -> Tuple[Tuple[MenuText]]:
                """sumary_line
                
                Keyword arguments:
                argument -- description
                Return: return_description

                TODO: Adjust sizes and test image initiliazation on video card vs cpu
                TODO: Adjust parameters
                """
                from pygame import Surface, HWSURFACE # pylint: disable=W,E, import-error, import-outside-toplevel, no-name-in-module
                from src.gui.menu_items.MenuText import MenuText # pylint: disable=W,E, import-error, import-outside-toplevel
                from src.gui.menu_items.MenuLabel import MenuLabel # pylint: disable=W,E, import-error, import-outside-toplevel
                from src.State import ButtonStateLookUpTable, MenuLabelStateLookUpTable # pylint: disable=W,E, import-error, import-outside-toplevel

                def create_options_text() -> MenuText:
                    """sumary_line
                    
                    Keyword arguments:
                    argument -- description
                    Return: return_description
                    """
                    options_text : MenuText = MenuText()
                    options_text.set_text = "OPTIONS"
                    options_text.set_mouse_state = ButtonStateLookUpTable.NOT_COLLIDE
                    options_text.set_punto = 12
                    options_text.pos_x = 10 + options_text.relative_width()
                    options_text.pos_y = 10

                    return options_text

                def create_magnitude_text() -> MenuText:
                    """sumary_line
                    
                    Keyword arguments:
                    argument -- description
                    Return: return_description
                    """
                    magnitude_text : MenuText = MenuText()
                    magnitude_text.init_elements()
                    magnitude_text.set_text = "5"
                    magnitude_text.set_mouse_state = ButtonStateLookUpTable.NOT_COLLIDE
                    magnitude_text.set_punto = 12
                    magnitude_text.pos_x = 190 - magnitude_text.relative_width()
                    magnitude_text.pos_y = 10

                    return magnitude_text

                def create_transparent_surface(size: Tuple[int,int]) -> Surface:
                    """sumary_line
                    
                    Keyword arguments:
                    argument -- description
                    Return: return_description
                    """
                    tmp_surface : Surface = Surface(size=size,flags=HWSURFACE)
                    tmp_surface.set_alpha(value=0,flags=HWSURFACE)

                    return tmp_surface

                def create_menu_label() -> MenuLabel:
                    """sumary_line
                    
                    Keyword arguments:
                    argument -- description
                    Return: return_description
                    """
                    options_text : MenuText = create_options_text()
                    magnitude_text : MenuText = create_magnitude_text()

                    space = 50
                    size = ((options_text.relative_pos()[0]+ space +magnitude_text.relative_pos[0]+10+magnitude_text.relative_width()),options_text.relative_height()+2*options_text.relative_pos[1])

                    tmp_surface:Surface = create_transparent_surface(size=size)

                    tmp_menu_label : MenuLabel = MenuLabel()
                    tmp_menu_label.init_elements(((tmp_surface,options_text,magnitude_text),))
                    tmp_menu_label.init_external_states(((MenuLabelStateLookUpTable.NOT_VISIBLE for _ in range(3)),))

                    return tmp_menu_label

                return create_menu_label()

            match button_no:

                case ButtonLookUpTable.SOUND_LEVEL_BUTTON:
                    return create_sound_level_button()
                case _ :
                    raise TypeError(f"Undefined button type {button_no.__name__}")

        def create_exit_button():  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        def create_start_button():  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        def create_confirm_button():  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        def create_resume_button():  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        def create_sound_on_off_button():  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        def create_star_button():  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        def command_start_button():  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        def command_star_button():  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        def command_exit_button():  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        def command_settings_button():  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        def command_sound_button():  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        def command_confirm_button():  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        def command_display_size_button():  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        def command_sound_level_button():  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        def command_sound_button():  # pylint: disable = W,E
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description
            """

            raise NotImplementedError

        match button_no:

            case ButtonLookUpTable.EXIT_BUTTON:
                return create_exit_button()
            case ButtonLookUpTable.START_BUTTON:
                return create_start_button()
            case ButtonLookUpTable.CONFIRM_BUTTON:
                return create_confirm_button()
            case ButtonLookUpTable.RESUME_BUTTON:
                return create_resume_button()
            case ButtonLookUpTable.SOUND_ON_OFF_BUTTON:
                return create_sound_on_off_button()
            case ButtonLookUpTable.STAR_BUTTON:
                return create_star_button()
            case _ :
                return create_text_button(button_no)

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
