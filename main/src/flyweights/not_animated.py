"""
This module contains NotAnimated flyweight class

TODO: Scale everthing when coding started

"""

from pygame.mixer import Sound
from pygame.font import Font
from pygame import image, transform

from .Flyweight import Flyweight


class NotAnimated(Flyweight):
    """
    This class is container for NotAnimated objects

    Keywords:
        "crosshair"
        "bgs_main_menu"
        "icons_skill"
        "start_menu_sound"
        "game_sound"
        "hearth"
        "shield"
        "W"
        "A"
        "S"
        "D"
        "elenore_face"
        "moonpie_face"
        "menu_box_long"
        "menu_box"
        "menu_shop"
        "icon_template"
        "icon_random"
        "chest_openning_sound"
        "chest_closing_sound"
        "click_sound"
        "buy_sound"
        "heart_sound"
        "death_sound"
        "font"
        "elenore_menu_voices"
        "elenore_demaged_voices"
        "elenore_healed_voices"
        "elenore_shield_voices"
        "moonpie_menu_voices"
        "moonpie_demaged_voices"
        "moonpie_healed_voices"
        "moonpie_shield_voices"
        "pygame_logo"
        "quest_logo"
    """

    Flyweight.data["crosshair"] = image.load(
        ".assets/Crosshairs/Outline/CrosshairsOutline17.png"
    )
    Flyweight.data["bgs_main_menu"] = (
        transform.scale_by(
            image.load(".assets/Desolate Places/Cloudy Mountains.png"), 3.0
        ),
        transform.scale_by(image.load(".assets/Desolate Places/Dusty Moon.png"), 3.0),
        transform.scale_by(
            image.load(".assets/Desolate Places/Hidden Desert.png"), 3.0
        ),
        transform.scale_by(image.load(".assets/Desolate Places/Misty Rocks.png"), 3.0),
        transform.scale_by(image.load(".assets/Desolate Places/Starry Peaks.png"), 3.0),
    )
    Flyweight.data["icons_skill"] = (
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons1.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons2.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons3.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons4.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons5.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons6.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons7.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons8.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons9.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons10.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons11.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons12.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons13.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons14.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons15.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons16.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons17.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons18.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons19.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons20.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons21.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons22.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons23.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons24.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons25.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons26.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons27.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons28.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons29.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons30.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons31.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons32.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons33.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons34.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons35.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons36.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons37.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons38.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons39.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons40.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons41.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons42.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons43.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons44.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons45.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons46.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons47.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons48.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons49.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons50.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons51.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons52.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons53.png"),
        image.load(".assets/skill_icons_by_quintino_pixels/96x96/skill_icons54.png"),
    )
    Flyweight.data["start_menu_sound"] = Sound(".assets/game_Sound/Spy/Spy.mp3")
    Flyweight.data["game_sound"] = (
        Sound(".assets/game_Sound/16_bit_space.ogg"),
        Sound(".assets/game_Sound/future.ogg"),
        Sound(".assets/game_Sound/glitch.ogg"),
        Sound(".assets/game_Sound/retro_metal.ogg"),
    )
    Flyweight.data["hearth"] = (
        image.load(".assets/health/heart_1.png"),
        image.load(".assets/health/heart_2.png"),
        image.load(".assets/health/heart_3.png"),
    )
    Flyweight.data["shield"] = (
        image.load(".assets/health/shield_1.png"),
        image.load(".assets/health/shield_2.png"),
        image.load(".assets/health/shield_3.png"),
    )
    Flyweight.data["W"] = image.load(".assets/Individual Icons/keyboard_14.png")
    Flyweight.data["A"] = image.load(".assets/Individual Icons/keyboard_23.png")
    Flyweight.data["S"] = image.load(".assets/Individual Icons/keyboard_24.png")
    Flyweight.data["D"] = image.load(".assets/Individual Icons/keyboard_25.png")
    Flyweight.data["elenore_face"] = image.load(".assets/pixel-ladies-free/002.png")
    Flyweight.data["moonpie_face"] = image.load(".assets/pixel-ladies-free/010.png")
    Flyweight.data["menu_box_long"] = image.load(
        ".assets/Simple UI Pack/Menu/64x64/InfoBox_3x4.png"
    )
    Flyweight.data["menu_box"] = image.load(
        ".assets/Simple UI Pack/Menu/64x64/InfoBox.png"
    )
    Flyweight.data["menu_shop"] = image.load(
        ".assets/Simple UI Pack/Menu/64x64/SHOP.png"
    )
    Flyweight.data["icon_template"] = transform.scale_by(
        image.load(
            ".assets/Simple UI Pack/Icons and Vectors/64x64/Icons/IconTemplate.png"
        ),
        1.6,
    )
    Flyweight.data["icon_random"] = image.load(
        ".assets/Simple UI Pack/Icons and Vectors/64x64/Icons/RandomBox.png"
    )
    Flyweight.data["chest_openning_sound"] = Sound(
        ".assets/SoundStarterPack/SoundStarterPack/Starter Pack-Realist Sound Bank.23/Chest/ChestOpening1.wav"
    )
    Flyweight.data["chest_closing_sound"] = Sound(
        ".assets/SoundStarterPack/SoundStarterPack/Starter Pack-Realist Sound Bank.23/Chest/ChestClosing2.wav"
    )
    Flyweight.data["click_sound"] = Sound(
        ".assets/SoundStarterPack/SoundStarterPack/Starter Pack-Realist Sound Bank.23/Click-Button-Switch/Click1.wav"
    )
    Flyweight.data["buy_sound"] = Sound(
        ".assets/SoundStarterPack/SoundStarterPack/Starter Pack-Realist Sound Bank.23/Coin/CoinDrop1.wav"
    )
    Flyweight.data["heart_sound"] = Sound(
        ".assets/SoundStarterPack/SoundStarterPack/Starter Pack-Realist Sound Bank.23/HeartBeat/HeartBeatFast1.wav"
    )
    Flyweight.data["death_sound"] = Sound(
        ".assets/SoundStarterPack/SoundStarterPack/Starter Pack-Realist Sound Bank.23/Hit(Impact)/HitGore1.wav"
    )
    Flyweight.data["font"] = Font(".assets/DungeonFont.ttf")
    Flyweight.data["elenore_menu_voices"] = (
        Sound(".assets/Elenore/Type 2/aqua.wav"),
        Sound(".assets/Elenore/Type 2/blizzard.wav"),
        Sound(".assets/Elenore/Type 2/bubbles.wav"),
        Sound(".assets/Elenore/Type 2/burn.wav"),
        Sound(".assets/Elenore/Type 2/curse.wav"),
        Sound(".assets/Elenore/Type 2/cyclone.wav"),
        Sound(".assets/Elenore/Type 2/fire.wav"),
        Sound(".assets/Elenore/Type 2/freeze.wav"),
        Sound(".assets/Elenore/Type 2/hellstorm.wav"),
        Sound(".assets/Elenore/Type 2/hex.wav"),
        Sound(".assets/Elenore/Type 2/ice.wav"),
        Sound(".assets/Elenore/Type 2/tornado.wav"),
        Sound(".assets/Elenore/Type 2/twister.wav"),
        Sound(".assets/Elenore/Type 2/water.wav"),
        Sound(".assets/Elenore/Type 2/wind.wav"),
    )
    Flyweight.data["elenore_demaged_voices"] = (
        Sound(".assets/Elenore/Type 2/damaged1.wav"),
        Sound(".assets/Elenore/Type 2/damaged2.wav"),
        Sound(".assets/Elenore/Type 2/damaged3.wav"),
    )
    Flyweight.data["elenore_healed_voices"] = (
        Sound(".assets/Elenore/Type 2/heal.wav"),
        Sound(".assets/Elenore/Type 2/healed1.wav"),
        Sound(".assets/Elenore/Type 2/healed2.wav"),
        Sound(".assets/Elenore/Type 2/healed3.wav"),
    )
    Flyweight.data["elenore_shield_voices"] = Sound(".assets/Elenore/Type 2/cure.wav")
    Flyweight.data["moonpie_menu_voices"] = (
        Sound(".assets/MoonPie/RPG Voice Starter Pack/Type 1/aqua.wav"),
        Sound(".assets/MoonPie/RPG Voice Starter Pack/Type 1/blizzard.wav"),
        Sound(".assets/MoonPie/RPG Voice Starter Pack/Type 1/bubbles.wav"),
        Sound(".assets/MoonPie/RPG Voice Starter Pack/Type 1/burn.wav"),
        Sound(".assets/MoonPie/RPG Voice Starter Pack/Type 1/curse.wav"),
        Sound(".assets/MoonPie/RPG Voice Starter Pack/Type 1/cyclone.wav"),
        Sound(".assets/MoonPie/RPG Voice Starter Pack/Type 1/fire.wav"),
        Sound(".assets/MoonPie/RPG Voice Starter Pack/Type 1/freeze.wav"),
        Sound(".assets/MoonPie/RPG Voice Starter Pack/Type 1/hellstorm.wav"),
        Sound(".assets/MoonPie/RPG Voice Starter Pack/Type 1/hex.wav"),
        Sound(".assets/MoonPie/RPG Voice Starter Pack/Type 1/ice.wav"),
        Sound(".assets/MoonPie/RPG Voice Starter Pack/Type 1/tornado.wav"),
        Sound(".assets/MoonPie/RPG Voice Starter Pack/Type 1/twister.wav"),
        Sound(".assets/MoonPie/RPG Voice Starter Pack/Type 1/water.wav"),
        Sound(".assets/MoonPie/RPG Voice Starter Pack/Type 1/wind.wav"),
    )
    Flyweight.data["moonpie_demaged_voices"] = (
        Sound(".assets/MoonPie/RPG Voice Starter Pack/Type 1/damaged1.wav"),
        Sound(".assets/MoonPie/RPG Voice Starter Pack/Type 1/damaged2.wav"),
        Sound(".assets/MoonPie/RPG Voice Starter Pack/Type 1/damaged3.wav"),
    )
    Flyweight.data["moonpie_healed_voices"] = (
        Sound(".assets/MoonPie/RPG Voice Starter Pack/Type 1/heal.wav"),
        Sound(".assets/MoonPie/RPG Voice Starter Pack/Type 1/healed1.wav"),
        Sound(".assets/MoonPie/RPG Voice Starter Pack/Type 1/healed2.wav"),
        Sound(".assets/MoonPie/RPG Voice Starter Pack/Type 1/healed3.wav"),
    )
    Flyweight.data["moonpie_shield_voices"] = Sound(
        ".assets/MoonPie/RPG Voice Starter Pack/Type 1/cure.wav"
    )
    Flyweight.data["pygame_logo"] = image.load(".img/pygame_powered.png")
    Flyweight.data["quest_logo"] = image.load(".img/quest_logo.png")
    # TODO: Add game texts
