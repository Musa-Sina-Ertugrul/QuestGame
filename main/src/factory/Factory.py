"""sumary_line

Keyword arguments:
argument -- description
Return: return_description

TODO: When implementations are done functions will be filled and object typing will be changed
TODO: Update Docstrings
"""
from enum import EnumType
from copy import copy
from typing import Tuple, Callable, Optional
from numpy import random
from pygame import mouse, display, event
from pygame.mixer import music
import pygame
from src.flyweights.not_animated import NotAnimated


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

        from src.gui.menu_items.MenuTemplate import (  # pylint: disable=W,E, import-error, import-outside-toplevel
            MenuTemplate,  # pylint: disable=W,E, import-error, import-outside-toplevel
        )  # pylint: disable=W,E, import-error, import-outside-toplevel

        return MenuTemplate()

    @staticmethod
    def create_guis():
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        from sys import (
            path,
        )  # pylint: disable=W,E, import-error, import-outside-toplevel

        path.append("main/src/")
        from Gui import (
            Gui,
        )  # pylint: disable=W,E, import-error, import-outside-toplevel

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

    # NOTE: For test this function become protected
    @staticmethod
    def _create_button(button_no: EnumType) -> object:  # pylint: disable = W,E
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description

        TODO: Add more text button

        """

        from src.State import (
            ButtonLookUpTable,
        )  # pylint: disable=W,E, import-error, import-outside-toplevel

        def create_text_button(button_no: EnumType):
            """sumary_line

            Keyword arguments:
            argument -- description
            Return: return_description

            TODO: Add more button

            """

            from src.gui.menu_items.MenuText import (  # pylint: disable=W,E, import-error, import-outside-toplevel, no-name-in-module
                MenuText,  # pylint: disable=W,E, import-error, import-outside-toplevel, no-name-in-module
            )  # pylint: disable=W,E, import-error, import-outside-toplevel

            def create_sound_level_button() -> Tuple[Tuple[MenuText]]:
                """sumary_line

                Keyword arguments:
                argument -- description
                Return: return_description

                TODO: Adjust sizes and test image initiliazation on video card vs cpu
                TODO: Adjust parameters
                """
                from pygame import (  # pylint: disable=W,E, import-error, import-outside-toplevel, no-name-in-module
                    Surface,  # pylint: disable=W,E, import-error, import-outside-toplevel, no-name-in-module
                    HWSURFACE,  # pylint: disable=W,E, import-error, import-outside-toplevel, no-name-in-module
                )  # pylint: disable=W,E, import-error, import-outside-toplevel, no-name-in-module
                from src.gui.menu_items.MenuText import (  # pylint: disable=W,E, import-error, import-outside-toplevel, no-name-in-module
                    MenuText,  # pylint: disable=W,E, import-error, import-outside-toplevel, no-name-in-module
                )  # pylint: disable=W,E, import-error, import-outside-toplevel
                from src.gui.menu_items.Button import (  # pylint: disable=W,E, import-error, import-outside-toplevel, no-name-in-module
                    Button,  # pylint: disable=W,E, import-error, import-outside-toplevel, no-name-in-module
                )  # pylint: disable=W,E, import-error, import-outside-toplevel
                from src.State import (  # pylint: disable=W,E, import-error, import-outside-toplevel, no-name-in-module
                    ButtonStateLookUpTable,  # pylint: disable=W,E, import-error, import-outside-toplevel, no-name-in-module
                )  # pylint: disable=W,E, import-error, import-outside-toplevel

                def create_options_text() -> MenuText:
                    """sumary_line

                    Keyword arguments:
                    argument -- description
                    Return: return_description
                    """
                    options_text: MenuText = MenuText()
                    options_text.set_text = "SOUND LEVEL"
                    options_text.init_external_states()
                    options_text.init_elements()
                    options_text.set_mouse_state = ButtonStateLookUpTable.NOT_COLLIDE
                    options_text.set_pos_x = 10
                    options_text.set_pos_y = 10

                    return options_text

                def create_magnitude_text() -> MenuText:
                    """sumary_line

                    Keyword arguments:
                    argument -- description
                    Return: return_description
                    """
                    magnitude_text: MenuText = MenuText()
                    magnitude_text.init_elements()
                    magnitude_text.init_external_states()
                    magnitude_text.set_text = "1.0"
                    magnitude_text.set_mouse_state = ButtonStateLookUpTable.NOT_COLLIDE
                    magnitude_text.set_pos_x = 190 - magnitude_text.relative_width()
                    magnitude_text.set_pos_y = 10

                    return magnitude_text

                def create_transparent_surface(size: Tuple[int, int]) -> Surface:
                    """sumary_line

                    Keyword arguments:
                    argument -- description
                    Return: return_description
                    """
                    tmp_surface: Surface = Surface(size, HWSURFACE)
                    # tmp_surface.set_alpha(0,HWSURFACE)

                    return tmp_surface

                def command_sound_level_button(
                    instance: Optional[MenuText | None] = False,
                ):
                    """Just holds magnitude variable for later calls

                    TODO: This function must work on seperate thread or process and sleep for some time

                    Args:
                        instance (Optinonal[MenuText]) : Initial argument to identify
                        magnitude text
                    """

                    def inner_command(instance: MenuText):
                        """Adjust volume based on mouse pos

                        Takes instance variable comes from outter function
                        and ajust volume then set text with setter

                        Args:
                            instance (MenuText) : Initial argument to identify
                            magnitude text
                        """
                        mouse_pos_x, _ = mouse.get_pos()
                        display_x, _ = display.get_desktop_sizes()[0]
                        current_volume: float = NotAnimated.data[
                            "click_sound"
                        ].get_volume()

                        if mouse_pos_x <= display_x // 2:
                            current_volume -= 0.1
                            if current_volume < 0.0:
                                current_volume = 0.0
                                try:
                                    raise RuntimeError("Sound level is at lowest")
                                except RuntimeError:
                                    print("Sound level is at lowest")

                            # TODO: All sounds will be add here

                        else:
                            current_volume += 0.1
                            if current_volume > 1.0:
                                current_volume = 1.0
                                # NOTE : Error has written for test cases, After test delete it
                                try:
                                    raise RuntimeError("Sound level is at highest")
                                except RuntimeError:
                                    print("Sound level is at highest")

                            # TODO: All sounds will be add here
                        NotAnimated.data["click_sound"].set_volume(current_volume)
                        NotAnimated.data["click_sound"].play()
                        instance.set_text = str(current_volume)

                    # NOTE: Function starts from here
                    if instance:
                        command_sound_level_button.instance = instance
                        print(command_sound_level_button.instance)
                        return

                    if mouse.get_pressed()[0]:
                        inner_command(command_sound_level_button.instance)

                def create_button() -> Button:
                    """sumary_line

                    Keyword arguments:
                    argument -- description
                    Return: return_description
                    """
                    options_text: MenuText = create_options_text()
                    magnitude_text: MenuText = create_magnitude_text()

                    size: Tuple[int, int] = (
                        (
                            20
                            + magnitude_text.relative_pos()[0]
                            + magnitude_text.relative_width()
                        ),
                        (options_text.relative_height() + 20),
                    )

                    tmp_surface: Surface = create_transparent_surface(size=size)

                    tmp_button: Button = Button()
                    command_sound_level_button(magnitude_text)
                    tmp_button.init_elements(
                        [[tmp_surface, options_text, magnitude_text]]
                    )
                    tmp_button.init_external_states(
                        [
                            [
                                ButtonStateLookUpTable.NULL,
                                ButtonStateLookUpTable.CLICKED,
                                ButtonStateLookUpTable.CLICKED,
                            ]
                        ]
                    )
                    tmp_button.set_func = command_sound_level_button
                    tmp_button.size_nultiplier = 2.0

                    return tmp_button

                # NOTE: create_sound_level_button() starts here

                return create_button()

            # NOTE: create_text_button(button_no: EnumType) starts here

            match button_no:
                case ButtonLookUpTable.SOUND_LEVEL_BUTTON:
                    return create_sound_level_button()
                case _:
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
            case _:
                return create_text_button(button_no)

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
