"""
    This file contains Flyweights as Prototype
    Flyweight class is an abstract class it has been
    inhereted by Animated and Not_Animated classes
    These two classes will contain assests as static
"""

from abc import ABC
from typing import Dict, List, Optional
from pygame import image
from pygame import Surface
from pygame.mixer import Sound
from pygame.font import Font


class Flyweight(ABC):
    """
    Data container for Flyweight objects

    This class is an abstract class and is inhereted by Animeted
    and NotAnimated classes

    Attributes:
        data (Dict[str, List[Surface]]) : contains Surface objects
    """

    data: Dict[str, List[Optional[Font | Sound | Surface]]] = {}


class Animated(Flyweight):
    """
    Data container for Animated Flywieght objects

    Keywords:
        "fire_cast"
        "ice_cast"
        "light_cast"
        "magic_cast"
        "crazy_chest"
        "gold_chest"
        "king_chest"
        "silver_chest"
        "dark_spell_1"
        "dark_spell_2"
        "elenore"
        "elenore_shadow"
        "eye_fire_blue"
        "eye_fire_red"
        "bat"
        "ghost"
        "lizard"
        "skeleton"
        "slime"
        "crab"
        "ice_spell_1_hit"
        "ice_spell_1_move"
        "ice_spell_1_strat"
        "ice_spell_2_active"
        "ice_spell_2_ending"
        "ice_spell_2_start"
        "npc_ranger"
        "npc_gunslinger"
        "npc_witch"
        "npc_king"
        "npc_monk"
        "npc_trader"
        "npc_fairy"
        "moonpie_front_idle"
        "moonpie_left_idle"
        "moonpie_right_idle"
        "moonpie_back_idle"
        "moonpie_front_run"
        "moonpie_left_run"
        "moonpie_right_run"
        "moonpie_back_run"
        "blood"
        "start_button"
        "exit_button"
        "coin"
        "confirm_button"
        "pause_button"
        "sound_button"
        "star_button"
        "shop_button"
        "you_button"
    """

    Flyweight.data["fire_cast"] = [  # use / instead of / if you are in windows !!!
        image.load(".assets/casts/fire_cast/FireCast_96x96_1.png"),
        image.load(".assets/casts/fire_cast/FireCast_96x96_2.png"),
        image.load(".assets/casts/fire_cast/FireCast_96x96_3.png"),
        image.load(".assets/casts/fire_cast/FireCast_96x96_4.png"),
        image.load(".assets/casts/fire_cast/FireCast_96x96_5.png"),
        image.load(".assets/casts/fire_cast/FireCast_96x96_6.png"),
        image.load(".assets/casts/fire_cast/FireCast_96x96_7.png"),
        image.load(".assets/casts/fire_cast/FireCast_96x96_8.png"),
        image.load(".assets/casts/fire_cast/FireCast_96x96_9.png"),
        image.load(".assets/casts/fire_cast/FireCast_96x96_10.png"),
        image.load(".assets/casts/fire_cast/FireCast_96x96_11.png"),
        image.load(".assets/casts/fire_cast/FireCast_96x96_12.png"),
        image.load(".assets/casts/fire_cast/FireCast_96x96_13.png"),
        image.load(".assets/casts/fire_cast/FireCast_96x96_14.png"),
        image.load(".assets/casts/fire_cast/FireCast_96x96_15.png"),
        image.load(".assets/casts/fire_cast/FireCast_96x96_16.png"),
        image.load(".assets/casts/fire_cast/FireCast_96x96_17.png"),
        image.load(".assets/casts/fire_cast/FireCast_96x96_18.png"),
        image.load(".assets/casts/fire_cast/FireCast_96x96_19.png"),
        image.load(".assets/casts/fire_cast/FireCast_96x96_20.png"),
        image.load(".assets/casts/fire_cast/FireCast_96x96_21.png"),
        image.load(".assets/casts/fire_cast/FireCast_96x96_22.png"),
        image.load(".assets/casts/fire_cast/FireCast_96x96_23.png"),
        image.load(".assets/casts/fire_cast/FireCast_96x96_24.png"),
        image.load(".assets/casts/fire_cast/FireCast_96x96_25.png"),
        image.load(".assets/casts/fire_cast/FireCast_96x96_26.png"),
        image.load(".assets/casts/fire_cast/FireCast_96x96_27.png"),
        image.load(".assets/casts/fire_cast/FireCast_96x96_28.png"),
    ]
    Flyweight.data["ice_cast"] = [
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_1.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_2.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_3.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_4.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_5.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_6.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_7.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_8.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_9.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_10.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_11.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_12.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_13.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_14.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_15.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_16.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_17.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_18.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_19.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_20.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_21.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_22.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_23.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_24.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_25.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_26.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_27.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_28.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_29.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_30.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_31.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_32.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_33.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_34.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_35.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_36.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_37.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_38.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_39.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_40.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_41.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_42.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_43.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_44.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_45.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_46.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_47.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_48.png"),
        image.load(".assets/casts/ice_shatter/IceShatter_96x96_49.png"),
    ]
    Flyweight.data["light_cast"] = [
        image.load(".assets/casts/light_cast/LightCast_96_1.png"),
        image.load(".assets/casts/light_cast/LightCast_96_2.png"),
        image.load(".assets/casts/light_cast/LightCast_96_3.png"),
        image.load(".assets/casts/light_cast/LightCast_96_4.png"),
        image.load(".assets/casts/light_cast/LightCast_96_5.png"),
        image.load(".assets/casts/light_cast/LightCast_96_6.png"),
        image.load(".assets/casts/light_cast/LightCast_96_7.png"),
        image.load(".assets/casts/light_cast/LightCast_96_8.png"),
        image.load(".assets/casts/light_cast/LightCast_96_9.png"),
        image.load(".assets/casts/light_cast/LightCast_96_10.png"),
        image.load(".assets/casts/light_cast/LightCast_96_11.png"),
        image.load(".assets/casts/light_cast/LightCast_96_12.png"),
        image.load(".assets/casts/light_cast/LightCast_96_13.png"),
        image.load(".assets/casts/light_cast/LightCast_96_14.png"),
        image.load(".assets/casts/light_cast/LightCast_96_15.png"),
        image.load(".assets/casts/light_cast/LightCast_96_16.png"),
        image.load(".assets/casts/light_cast/LightCast_96_17.png"),
        image.load(".assets/casts/light_cast/LightCast_96_18.png"),
        image.load(".assets/casts/light_cast/LightCast_96_19.png"),
        image.load(".assets/casts/light_cast/LightCast_96_20.png"),
        image.load(".assets/casts/light_cast/LightCast_96_21.png"),
        image.load(".assets/casts/light_cast/LightCast_96_22.png"),
        image.load(".assets/casts/light_cast/LightCast_96_23.png"),
        image.load(".assets/casts/light_cast/LightCast_96_24.png"),
        image.load(".assets/casts/light_cast/LightCast_96_25.png"),
        image.load(".assets/casts/light_cast/LightCast_96_26.png"),
        image.load(".assets/casts/light_cast/LightCast_96_27.png"),
        image.load(".assets/casts/light_cast/LightCast_96_28.png"),
        image.load(".assets/casts/light_cast/LightCast_96_29.png"),
        image.load(".assets/casts/light_cast/LightCast_96_30.png"),
        image.load(".assets/casts/light_cast/LightCast_96_31.png"),
        image.load(".assets/casts/light_cast/LightCast_96_32.png"),
        image.load(".assets/casts/light_cast/LightCast_96_33.png"),
        image.load(".assets/casts/light_cast/LightCast_96_34.png"),
        image.load(".assets/casts/light_cast/LightCast_96_35.png"),
        image.load(".assets/casts/light_cast/LightCast_96_36.png"),
        image.load(".assets/casts/light_cast/LightCast_96_37.png"),
        image.load(".assets/casts/light_cast/LightCast_96_38.png"),
        image.load(".assets/casts/light_cast/LightCast_96_39.png"),
        image.load(".assets/casts/light_cast/LightCast_96_40.png"),
        image.load(".assets/casts/light_cast/LightCast_96_41.png"),
        image.load(".assets/casts/light_cast/LightCast_96_42.png"),
        image.load(".assets/casts/light_cast/LightCast_96_43.png"),
        image.load(".assets/casts/light_cast/LightCast_96_44.png"),
        image.load(".assets/casts/light_cast/LightCast_96_45.png"),
        image.load(".assets/casts/light_cast/LightCast_96_46.png"),
        image.load(".assets/casts/light_cast/LightCast_96_47.png"),
        image.load(".assets/casts/light_cast/LightCast_96_48.png"),
    ]
    Flyweight.data["magic_cast"] = [
        image.load(".assets/casts/magic_barrier/MagicBarrier_64x64_1.png"),
        image.load(".assets/casts/magic_barrier/MagicBarrier_64x64_2.png"),
        image.load(".assets/casts/magic_barrier/MagicBarrier_64x64_3.png"),
        image.load(".assets/casts/magic_barrier/MagicBarrier_64x64_4.png"),
        image.load(".assets/casts/magic_barrier/MagicBarrier_64x64_5.png"),
        image.load(".assets/casts/magic_barrier/MagicBarrier_64x64_6.png"),
        image.load(".assets/casts/magic_barrier/MagicBarrier_64x64_7.png"),
        image.load(".assets/casts/magic_barrier/MagicBarrier_64x64_8.png"),
        image.load(".assets/casts/magic_barrier/MagicBarrier_64x64_9.png"),
        image.load(".assets/casts/magic_barrier/MagicBarrier_64x64_10.png"),
        image.load(".assets/casts/magic_barrier/MagicBarrier_64x64_11.png"),
        image.load(".assets/casts/magic_barrier/MagicBarrier_64x64_12.png"),
        image.load(".assets/casts/magic_barrier/MagicBarrier_64x64_13.png"),
        image.load(".assets/casts/magic_barrier/MagicBarrier_64x64_14.png"),
        image.load(".assets/casts/magic_barrier/MagicBarrier_64x64_15.png"),
        image.load(".assets/casts/magic_barrier/MagicBarrier_64x64_16.png"),
        image.load(".assets/casts/magic_barrier/MagicBarrier_64x64_17.png"),
        image.load(".assets/casts/magic_barrier/MagicBarrier_64x64_18.png"),
        image.load(".assets/casts/magic_barrier/MagicBarrier_64x64_19.png"),
        image.load(".assets/casts/magic_barrier/MagicBarrier_64x64_20.png"),
        image.load(".assets/casts/magic_barrier/MagicBarrier_64x64_21.png"),
        image.load(".assets/casts/magic_barrier/MagicBarrier_64x64_21.png"),
        image.load(".assets/casts/magic_barrier/MagicBarrier_64x64_22.png"),
        image.load(".assets/casts/magic_barrier/MagicBarrier_64x64_23.png"),
        image.load(".assets/casts/magic_barrier/MagicBarrier_64x64_24.png"),
        image.load(".assets/casts/magic_barrier/MagicBarrier_64x64_25.png"),
        image.load(".assets/casts/magic_barrier/MagicBarrier_64x64_26.png"),
        image.load(".assets/casts/magic_barrier/MagicBarrier_64x64_27.png"),
        image.load(".assets/casts/magic_barrier/MagicBarrier_64x64_28.png"),
        image.load(".assets/casts/magic_barrier/MagicBarrier_64x64_29.png"),
        image.load(".assets/casts/magic_barrier/MagicBarrier_64x64_30.png"),
        image.load(".assets/casts/magic_barrier/MagicBarrier_64x64_31.png"),
        image.load(".assets/casts/magic_barrier/MagicBarrier_64x64_32.png"),
        image.load(".assets/casts/magic_barrier/MagicBarrier_64x64_33.png"),
    ]
    Flyweight.data["crazy_chest"] = [
        image.load(".assets/chests/crazy/Layer-1.png"),
        image.load(".assets/chests/crazy/Layer-2.png"),
        image.load(".assets/chests/crazy/Layer-3.png"),
        image.load(".assets/chests/crazy/Layer-4.png"),
        image.load(".assets/chests/crazy/Layer-5.png"),
        image.load(".assets/chests/crazy/Layer-6.png"),
        image.load(".assets/chests/crazy/Layer-7.png"),
        image.load(".assets/chests/crazy/Layer-8.png"),
    ]
    Flyweight.data["gold_chest"] = [
        image.load(".assets/chests/gold/Layer-1.png"),
        image.load(".assets/chests/gold/Layer-2.png"),
        image.load(".assets/chests/gold/Layer-3.png"),
        image.load(".assets/chests/gold/Layer-4.png"),
        image.load(".assets/chests/gold/Layer-5.png"),
        image.load(".assets/chests/gold/Layer-6.png"),
        image.load(".assets/chests/gold/Layer-7.png"),
        image.load(".assets/chests/gold/Layer-8.png"),
    ]
    Flyweight.data["king_chest"] = [
        image.load(".assets/chests/KING/Layer-1.png"),
        image.load(".assets/chests/KING/Layer-2.png"),
        image.load(".assets/chests/KING/Layer-3.png"),
        image.load(".assets/chests/KING/Layer-4.png"),
        image.load(".assets/chests/KING/Layer-5.png"),
        image.load(".assets/chests/KING/Layer-6.png"),
        image.load(".assets/chests/KING/Layer-7.png"),
        image.load(".assets/chests/KING/Layer-8.png"),
    ]
    Flyweight.data["silver_chest"] = [
        image.load(".assets/chests/Silver/Layer-1.png"),
        image.load(".assets/chests/Silver/Layer-2.png"),
        image.load(".assets/chests/Silver/Layer-3.png"),
        image.load(".assets/chests/Silver/Layer-4.png"),
        image.load(".assets/chests/Silver/Layer-5.png"),
        image.load(".assets/chests/Silver/Layer-6.png"),
        image.load(".assets/chests/Silver/Layer-7.png"),
        image.load(".assets/chests/Silver/Layer-8.png"),
    ]
    Flyweight.data["dark_spell_1"] = [
        image.load(
            ".assets/Dark VFX 01 - 02/Dark VFX 1/Separeted frames/Dark VFX 1 (40x32)1.png"
        ),
        image.load(
            ".assets/Dark VFX 01 - 02/Dark VFX 1/Separeted frames/Dark VFX 1 (40x32)2.png"
        ),
        image.load(
            ".assets/Dark VFX 01 - 02/Dark VFX 1/Separeted frames/Dark VFX 1 (40x32)3.png"
        ),
        image.load(
            ".assets/Dark VFX 01 - 02/Dark VFX 1/Separeted frames/Dark VFX 1 (40x32)4.png"
        ),
        image.load(
            ".assets/Dark VFX 01 - 02/Dark VFX 1/Separeted frames/Dark VFX 1 (40x32)5.png"
        ),
        image.load(
            ".assets/Dark VFX 01 - 02/Dark VFX 1/Separeted frames/Dark VFX 1 (40x32)6.png"
        ),
        image.load(
            ".assets/Dark VFX 01 - 02/Dark VFX 1/Separeted frames/Dark VFX 1 (40x32)7.png"
        ),
        image.load(
            ".assets/Dark VFX 01 - 02/Dark VFX 1/Separeted frames/Dark VFX 1 (40x32)8.png"
        ),
        image.load(
            ".assets/Dark VFX 01 - 02/Dark VFX 1/Separeted frames/Dark VFX 1 (40x32)9.png"
        ),
        image.load(
            ".assets/Dark VFX 01 - 02/Dark VFX 1/Separeted frames/Dark VFX 1 (40x32)10.png"
        ),
        image.load(
            ".assets/Dark VFX 01 - 02/Dark VFX 1/Separeted frames/Dark VFX 1 (40x32)11.png"
        ),
        image.load(
            ".assets/Dark VFX 01 - 02/Dark VFX 1/Separeted frames/Dark VFX 1 (40x32)12.png"
        ),
        image.load(
            ".assets/Dark VFX 01 - 02/Dark VFX 1/Separeted frames/Dark VFX 1 (40x32)13.png"
        ),
        image.load(
            ".assets/Dark VFX 01 - 02/Dark VFX 1/Separeted frames/Dark VFX 1 (40x32)14.png"
        ),
        image.load(
            ".assets/Dark VFX 01 - 02/Dark VFX 1/Separeted frames/Dark VFX 1 (40x32)15.png"
        ),
        image.load(
            ".assets/Dark VFX 01 - 02/Dark VFX 1/Separeted frames/Dark VFX 1 (40x32)16.png"
        ),
        image.load(
            ".assets/Dark VFX 01 - 02/Dark VFX 1/Separeted frames/Dark VFX 1 (40x32)17.png"
        ),
    ]
    Flyweight.data["dark_spell_2"] = [
        image.load(
            ".assets/Dark VFX 01 - 02/Dark VFX 2/Separated Frames/Dark VFX 2 (48x64)1.png"
        ),
        image.load(
            ".assets/Dark VFX 01 - 02/Dark VFX 2/Separated Frames/Dark VFX 2 (48x64)2.png"
        ),
        image.load(
            ".assets/Dark VFX 01 - 02/Dark VFX 2/Separated Frames/Dark VFX 2 (48x64)3.png"
        ),
        image.load(
            ".assets/Dark VFX 01 - 02/Dark VFX 2/Separated Frames/Dark VFX 2 (48x64)4.png"
        ),
        image.load(
            ".assets/Dark VFX 01 - 02/Dark VFX 2/Separated Frames/Dark VFX 2 (48x64)5.png"
        ),
        image.load(
            ".assets/Dark VFX 01 - 02/Dark VFX 2/Separated Frames/Dark VFX 2 (48x64)6.png"
        ),
        image.load(
            ".assets/Dark VFX 01 - 02/Dark VFX 2/Separated Frames/Dark VFX 2 (48x64)7.png"
        ),
        image.load(
            ".assets/Dark VFX 01 - 02/Dark VFX 2/Separated Frames/Dark VFX 2 (48x64)8.png"
        ),
        image.load(
            ".assets/Dark VFX 01 - 02/Dark VFX 2/Separated Frames/Dark VFX 2 (48x64)9.png"
        ),
        image.load(
            ".assets/Dark VFX 01 - 02/Dark VFX 2/Separated Frames/Dark VFX 2 (48x64)10.png"
        ),
        image.load(
            ".assets/Dark VFX 01 - 02/Dark VFX 2/Separated Frames/Dark VFX 2 (48x64)11.png"
        ),
        image.load(
            ".assets/Dark VFX 01 - 02/Dark VFX 2/Separated Frames/Dark VFX 2 (48x64)12.png"
        ),
        image.load(
            ".assets/Dark VFX 01 - 02/Dark VFX 2/Separated Frames/Dark VFX 2 (48x64)13.png"
        ),
        image.load(
            ".assets/Dark VFX 01 - 02/Dark VFX 2/Separated Frames/Dark VFX 2 (48x64)14.png"
        ),
        image.load(
            ".assets/Dark VFX 01 - 02/Dark VFX 2/Separated Frames/Dark VFX 2 (48x64)15.png"
        ),
        image.load(
            ".assets/Dark VFX 01 - 02/Dark VFX 2/Separated Frames/Dark VFX 2 (48x64)16.png"
        ),
    ]
    Flyweight.data["elenore"] = [
        image.load(".assets/Elenore/Idle/Idle1.png"),
        image.load(".assets/Elenore/Idle/Idle2.png"),
        image.load(".assets/Elenore/Idle/Idle3.png"),
        image.load(".assets/Elenore/Idle/Idle4.png"),
        image.load(".assets/Elenore/Idle/Idle5.png"),
        image.load(".assets/Elenore/Idle/Idle6.png"),
        image.load(".assets/Elenore/Idle/Idle7.png"),
        image.load(".assets/Elenore/Idle/Idle8.png"),
        image.load(".assets/Elenore/Idle/Idle9.png"),
    ]
    Flyweight.data["elenore_shadow"] = [
        image.load(".assets/Elenore/Idle/Shadow/Shadow1.png"),
        image.load(".assets/Elenore/Idle/Shadow/Shadow2.png"),
        image.load(".assets/Elenore/Idle/Shadow/Shadow3.png"),
        image.load(".assets/Elenore/Idle/Shadow/Shadow4.png"),
        image.load(".assets/Elenore/Idle/Shadow/Shadow5.png"),
        image.load(".assets/Elenore/Idle/Shadow/Shadow6.png"),
        image.load(".assets/Elenore/Idle/Shadow/Shadow7.png"),
        image.load(".assets/Elenore/Idle/Shadow/Shadow8.png"),
        image.load(".assets/Elenore/Idle/Shadow/Shadow9.png"),
    ]
    Flyweight.data["eye_fire_blue"] = [
        image.load(".assets/enemies/Eye Fire Blue/eye fire blue1.png"),
        image.load(".assets/enemies/Eye Fire Blue/eye fire blue2.png"),
        image.load(".assets/enemies/Eye Fire Blue/eye fire blue3.png"),
        image.load(".assets/enemies/Eye Fire Blue/eye fire blue4.png"),
        image.load(".assets/enemies/Eye Fire Blue/eye fire blue5.png"),
        image.load(".assets/enemies/Eye Fire Blue/eye fire blue6.png"),
        image.load(".assets/enemies/Eye Fire Blue/eye fire blue7.png"),
    ]
    Flyweight.data["eye_fire_red"] = [
        image.load(".assets/enemies/Eye Fire Red/eye fire1.png"),
        image.load(".assets/enemies/Eye Fire Red/eye fire2.png"),
        image.load(".assets/enemies/Eye Fire Red/eye fire3.png"),
        image.load(".assets/enemies/Eye Fire Red/eye fire4.png"),
        image.load(".assets/enemies/Eye Fire Red/eye fire5.png"),
        image.load(".assets/enemies/Eye Fire Red/eye fire6.png"),
        image.load(".assets/enemies/Eye Fire Red/eye fire7.png"),
    ]
    Flyweight.data["bat"] = [
        image.load(".assets/enemies/sprites/Bat/bat1.png"),
        image.load(".assets/enemies/sprites/Bat/bat2.png"),
        image.load(".assets/enemies/sprites/Bat/bat3.png"),
        image.load(".assets/enemies/sprites/Bat/bat4.png"),
        image.load(".assets/enemies/sprites/Bat/bat5.png"),
    ]
    Flyweight.data["ghost"] = [
        image.load(".assets/enemies/sprites/Ghost/ghost1.png"),
        image.load(".assets/enemies/sprites/Ghost/ghost2.png"),
        image.load(".assets/enemies/sprites/Ghost/ghost3.png"),
        image.load(".assets/enemies/sprites/Ghost/ghost4.png"),
        image.load(".assets/enemies/sprites/Ghost/ghost5.png"),
    ]
    Flyweight.data["lizard"] = [
        image.load(".assets/enemies/sprites/lizard moves/lizard-move1.png"),
        image.load(".assets/enemies/sprites/lizard moves/lizard-move2.png"),
        image.load(".assets/enemies/sprites/lizard moves/lizard-move3.png"),
    ]
    Flyweight.data["skeleton"] = [
        image.load(".assets/enemies/sprites/Skeleton-Walk/skeleton-walk1.png"),
        image.load(".assets/enemies/sprites/Skeleton-Walk/skeleton-walk2.png"),
        image.load(".assets/enemies/sprites/Skeleton-Walk/skeleton-walk3.png"),
        image.load(".assets/enemies/sprites/Skeleton-Walk/skeleton-walk4.png"),
        image.load(".assets/enemies/sprites/Skeleton-Walk/skeleton-walk5.png"),
        image.load(".assets/enemies/sprites/Skeleton-Walk/skeleton-walk6.png"),
        image.load(".assets/enemies/sprites/Skeleton-Walk/skeleton-walk7.png"),
        image.load(".assets/enemies/sprites/Skeleton-Walk/skeleton-walk8.png"),
    ]
    Flyweight.data["slime"] = [
        image.load(".assets/enemies/sprites/Slime/slime1.png"),
        image.load(".assets/enemies/sprites/Slime/slime2.png"),
        image.load(".assets/enemies/sprites/Slime/slime3.png"),
        image.load(".assets/enemies/sprites/Slime/slime4.png"),
        image.load(".assets/enemies/sprites/Slime/slime5.png"),
    ]
    Flyweight.data["crab"] = [
        image.load(".assets/enemies/sprites/Walk/crab-walk1.png"),
        image.load(".assets/enemies/sprites/Walk/crab-walk2.png"),
        image.load(".assets/enemies/sprites/Walk/crab-walk3.png"),
        image.load(".assets/enemies/sprites/Walk/crab-walk4.png"),
        image.load(".assets/enemies/sprites/Walk/crab-walk5.png"),
        image.load(".assets/enemies/sprites/Walk/crab-walk6.png"),
    ]
    Flyweight.data["ice_spell_1_hit"] = [
        image.load(".assets/Ice Effect 01/Ice VFX 1/Separated Frames/VFX 1 Hit1.png"),
        image.load(".assets/Ice Effect 01/Ice VFX 1/Separated Frames/VFX 1 Hit2.png"),
        image.load(".assets/Ice Effect 01/Ice VFX 1/Separated Frames/VFX 1 Hit3.png"),
        image.load(".assets/Ice Effect 01/Ice VFX 1/Separated Frames/VFX 1 Hit4.png"),
        image.load(".assets/Ice Effect 01/Ice VFX 1/Separated Frames/VFX 1 Hit5.png"),
        image.load(".assets/Ice Effect 01/Ice VFX 1/Separated Frames/VFX 1 Hit6.png"),
        image.load(".assets/Ice Effect 01/Ice VFX 1/Separated Frames/VFX 1 Hit7.png"),
        image.load(".assets/Ice Effect 01/Ice VFX 1/Separated Frames/VFX 1 Hit8.png"),
    ]
    Flyweight.data["ice_spell_1_move"] = [
        image.load(
            ".assets/Ice Effect 01/Ice VFX 1/Separated Frames/VFX 1 Repeatable1.png"
        ),
        image.load(
            ".assets/Ice Effect 01/Ice VFX 1/Separated Frames/VFX 1 Repeatable2.png"
        ),
        image.load(
            ".assets/Ice Effect 01/Ice VFX 1/Separated Frames/VFX 1 Repeatable3.png"
        ),
        image.load(
            ".assets/Ice Effect 01/Ice VFX 1/Separated Frames/VFX 1 Repeatable4.png"
        ),
        image.load(
            ".assets/Ice Effect 01/Ice VFX 1/Separated Frames/VFX 1 Repeatable5.png"
        ),
        image.load(
            ".assets/Ice Effect 01/Ice VFX 1/Separated Frames/VFX 1 Repeatable6.png"
        ),
        image.load(
            ".assets/Ice Effect 01/Ice VFX 1/Separated Frames/VFX 1 Repeatable7.png"
        ),
        image.load(
            ".assets/Ice Effect 01/Ice VFX 1/Separated Frames/VFX 1 Repeatable8.png"
        ),
        image.load(
            ".assets/Ice Effect 01/Ice VFX 1/Separated Frames/VFX 1 Repeatable9.png"
        ),
        image.load(
            ".assets/Ice Effect 01/Ice VFX 1/Separated Frames/VFX 1 Repeatable10.png"
        ),
    ]
    Flyweight.data["ice_spell_1_strat"] = [
        image.load(".assets/Ice Effect 01/Ice VFX 1/Separated Frames/VFX 1 Start1.png"),
        image.load(".assets/Ice Effect 01/Ice VFX 1/Separated Frames/VFX 1 Start2.png"),
        image.load(".assets/Ice Effect 01/Ice VFX 1/Separated Frames/VFX 1 Start3.png"),
    ]
    Flyweight.data["ice_spell_2_active"] = [
        image.load(
            ".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Active1.png"
        ),
        image.load(
            ".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Active2.png"
        ),
        image.load(
            ".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Active3.png"
        ),
        image.load(
            ".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Active4.png"
        ),
        image.load(
            ".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Active5.png"
        ),
        image.load(
            ".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Active6.png"
        ),
        image.load(
            ".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Active7.png"
        ),
        image.load(
            ".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Active8.png"
        ),
        image.load(
            ".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Active9.png"
        ),
    ]
    Flyweight.data["ice_spell_2_ending"] = [
        image.load(
            ".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Ending1.png"
        ),
        image.load(
            ".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Ending2.png"
        ),
        image.load(
            ".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Ending3.png"
        ),
        image.load(
            ".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Ending4.png"
        ),
        image.load(
            ".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Ending5.png"
        ),
        image.load(
            ".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Ending6.png"
        ),
        image.load(
            ".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Ending7.png"
        ),
        image.load(
            ".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Ending8.png"
        ),
        image.load(
            ".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Ending9.png"
        ),
        image.load(
            ".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Ending11.png"
        ),
        image.load(
            ".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Ending12.png"
        ),
        image.load(
            ".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Ending13.png"
        ),
        image.load(
            ".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Ending14.png"
        ),
        image.load(
            ".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Ending15.png"
        ),
        image.load(
            ".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Ending16.png"
        ),
        image.load(
            ".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Ending17.png"
        ),
        image.load(
            ".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Ending18.png"
        ),
    ]
    Flyweight.data["ice_spell_2_start"] = [
        image.load(
            ".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Start1.png"
        ),
        image.load(
            ".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Start2.png"
        ),
        image.load(
            ".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Start3.png"
        ),
        image.load(
            ".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Start4.png"
        ),
        image.load(
            ".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Start5.png"
        ),
        image.load(
            ".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Start6.png"
        ),
        image.load(
            ".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Start7.png"
        ),
        image.load(
            ".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Start8.png"
        ),
        image.load(
            ".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Start9.png"
        ),
    ]
    Flyweight.data["npc_ranger"] = [
        image.load(
            ".assets/Lively_NPCs_v3.0/individual sprites/elementals/leaf_ranger/leaf_ranger_1.png"
        ),
        image.load(
            ".assets/Lively_NPCs_v3.0/individual sprites/elementals/leaf_ranger/leaf_ranger_2.png"
        ),
        image.load(
            ".assets/Lively_NPCs_v3.0/individual sprites/elementals/leaf_ranger/leaf_ranger_3.png"
        ),
        image.load(
            ".assets/Lively_NPCs_v3.0/individual sprites/elementals/leaf_ranger/leaf_ranger_4.png"
        ),
    ]
    Flyweight.data["npc_gunslinger"] = [
        image.load(
            ".assets/Lively_NPCs_v3.0/individual sprites/steampunk/gunslinger/gunslinger_1.png"
        ),
        image.load(
            ".assets/Lively_NPCs_v3.0/individual sprites/steampunk/gunslinger/gunslinger_2.png"
        ),
        image.load(
            ".assets/Lively_NPCs_v3.0/individual sprites/steampunk/gunslinger/gunslinger_3.png"
        ),
        image.load(
            ".assets/Lively_NPCs_v3.0/individual sprites/steampunk/gunslinger/gunslinger_4.png"
        ),
        image.load(
            ".assets/Lively_NPCs_v3.0/individual sprites/steampunk/gunslinger/gunslinger_5.png"
        ),
    ]
    Flyweight.data["npc_witch"] = [
        image.load(
            ".assets/Lively_NPCs_v3.0/individual sprites/medieval/witch/witch_00.png"
        ),
        image.load(
            ".assets/Lively_NPCs_v3.0/individual sprites/medieval/witch/witch_01.png"
        ),
        image.load(
            ".assets/Lively_NPCs_v3.0/individual sprites/medieval/witch/witch_02.png"
        ),
        image.load(
            ".assets/Lively_NPCs_v3.0/individual sprites/medieval/witch/witch_03.png"
        ),
        image.load(
            ".assets/Lively_NPCs_v3.0/individual sprites/medieval/witch/witch_04.png"
        ),
    ]
    Flyweight.data["npc_king"] = [
        image.load(
            ".assets/Lively_NPCs_v3.0/individual sprites/medieval/king/king_00.png"
        ),
        image.load(
            ".assets/Lively_NPCs_v3.0/individual sprites/medieval/king/king_01.png"
        ),
        image.load(
            ".assets/Lively_NPCs_v3.0/individual sprites/medieval/king/king_02.png"
        ),
        image.load(
            ".assets/Lively_NPCs_v3.0/individual sprites/medieval/king/king_03.png"
        ),
        image.load(
            ".assets/Lively_NPCs_v3.0/individual sprites/medieval/king/king_04.png"
        ),
    ]
    Flyweight.data["npc_monk"] = [
        image.load(
            ".assets/Lively_NPCs_v3.0/individual sprites/elementals/ground_monk/ground_monk_1.png"
        ),
        image.load(
            ".assets/Lively_NPCs_v3.0/individual sprites/elementals/ground_monk/ground_monk_2.png"
        ),
        image.load(
            ".assets/Lively_NPCs_v3.0/individual sprites/elementals/ground_monk/ground_monk_3.png"
        ),
        image.load(
            ".assets/Lively_NPCs_v3.0/individual sprites/elementals/ground_monk/ground_monk_4.png"
        ),
    ]
    Flyweight.data["npc_trader"] = [
        image.load(
            ".assets/Lively_NPCs_v3.0/individual sprites/steampunk/trader/trader_1.png"
        ),
        image.load(
            ".assets/Lively_NPCs_v3.0/individual sprites/steampunk/trader/trader_2.png"
        ),
        image.load(
            ".assets/Lively_NPCs_v3.0/individual sprites/steampunk/trader/trader_3.png"
        ),
        image.load(
            ".assets/Lively_NPCs_v3.0/individual sprites/steampunk/trader/trader_4.png"
        ),
    ]
    Flyweight.data["npc_fairy"] = [
        image.load(
            ".assets/Lively_NPCs_v3.0/individual sprites/medieval/fairy/fairy_1.png"
        ),
        image.load(
            ".assets/Lively_NPCs_v3.0/individual sprites/medieval/fairy/fairy_2.png"
        ),
        image.load(
            ".assets/Lively_NPCs_v3.0/individual sprites/medieval/fairy/fairy_3.png"
        ),
        image.load(
            ".assets/Lively_NPCs_v3.0/individual sprites/medieval/fairy/fairy_4.png"
        ),
    ]
    Flyweight.data["moonpie_front_idle"] = [
        image.load(".assets/MoonPie/girl_frames1.png"),
        image.load(".assets/MoonPie/girl_frames2.png"),
        image.load(".assets/MoonPie/girl_frames3.png"),
        image.load(".assets/MoonPie/girl_frames4.png"),
    ]
    Flyweight.data["moonpie_left_idle"] = [
        image.load(".assets/MoonPie/girl_frames5.png"),
        image.load(".assets/MoonPie/girl_frames6.png"),
        image.load(".assets/MoonPie/girl_frames7.png"),
        image.load(".assets/MoonPie/girl_frames8.png"),
    ]
    Flyweight.data["moonpie_right_idle"] = [
        image.load(".assets/MoonPie/girl_frames9.png"),
        image.load(".assets/MoonPie/girl_frames10.png"),
        image.load(".assets/MoonPie/girl_frames11.png"),
        image.load(".assets/MoonPie/girl_frames12.png"),
    ]
    Flyweight.data["moonpie_back_idle"] = [
        image.load(".assets/MoonPie/girl_frames13.png"),
        image.load(".assets/MoonPie/girl_frames14.png"),
        image.load(".assets/MoonPie/girl_frames15.png"),
        image.load(".assets/MoonPie/girl_frames16.png"),
    ]
    Flyweight.data["moonpie_front_run"] = [
        image.load(".assets/MoonPie/girl_frames17.png"),
        image.load(".assets/MoonPie/girl_frames18.png"),
        image.load(".assets/MoonPie/girl_frames19.png"),
        image.load(".assets/MoonPie/girl_frames20.png"),
        image.load(".assets/MoonPie/girl_frames21.png"),
        image.load(".assets/MoonPie/girl_frames22.png"),
    ]
    Flyweight.data["moonpie_left_run"] = [
        image.load(".assets/MoonPie/girl_frames23.png"),
        image.load(".assets/MoonPie/girl_frames24.png"),
        image.load(".assets/MoonPie/girl_frames25.png"),
        image.load(".assets/MoonPie/girl_frames26.png"),
        image.load(".assets/MoonPie/girl_frames27.png"),
        image.load(".assets/MoonPie/girl_frames28.png"),
    ]
    Flyweight.data["moonpie_right_run"] = [
        image.load(".assets/MoonPie/girl_frames29.png"),
        image.load(".assets/MoonPie/girl_frames30.png"),
        image.load(".assets/MoonPie/girl_frames31.png"),
        image.load(".assets/MoonPie/girl_frames32.png"),
        image.load(".assets/MoonPie/girl_frames33.png"),
        image.load(".assets/MoonPie/girl_frames34.png"),
    ]
    Flyweight.data["moonpie_back_run"] = [
        image.load(".assets/MoonPie/girl_frames35.png"),
        image.load(".assets/MoonPie/girl_frames36.png"),
        image.load(".assets/MoonPie/girl_frames37.png"),
        image.load(".assets/MoonPie/girl_frames38.png"),
        image.load(".assets/MoonPie/girl_frames39.png"),
        image.load(".assets/MoonPie/girl_frames40.png"),
    ]
    Flyweight.data["moonpie_death"] = [
        image.load(".assets/MoonPie/girl_frames41.png"),
        image.load(".assets/MoonPie/girl_frames42.png"),
        image.load(".assets/MoonPie/girl_frames43.png"),
        image.load(".assets/MoonPie/girl_frames44.png"),
    ]
    Flyweight.data["blood"] = [
        image.load(".assets/NEw pack blood/1/1_0.png"),
        image.load(".assets/NEw pack blood/1/1_1.png"),
        image.load(".assets/NEw pack blood/1/1_2.png"),
        image.load(".assets/NEw pack blood/1/1_3.png"),
        image.load(".assets/NEw pack blood/1/1_4.png"),
        image.load(".assets/NEw pack blood/1/1_5.png"),
        image.load(".assets/NEw pack blood/1/1_6.png"),
        image.load(".assets/NEw pack blood/1/1_7.png"),
        image.load(".assets/NEw pack blood/1/1_8.png"),
        image.load(".assets/NEw pack blood/1/1_9.png"),
        image.load(".assets/NEw pack blood/1/1_10.png"),
        image.load(".assets/NEw pack blood/1/1_11.png"),
        image.load(".assets/NEw pack blood/1/1_12.png"),
        image.load(".assets/NEw pack blood/1/1_13.png"),
        image.load(".assets/NEw pack blood/1/1_14.png"),
        image.load(".assets/NEw pack blood/1/1_15.png"),
        image.load(".assets/NEw pack blood/1/1_16.png"),
        image.load(".assets/NEw pack blood/1/1_17.png"),
        image.load(".assets/NEw pack blood/1/1_18.png"),
        image.load(".assets/NEw pack blood/1/1_19.png"),
        image.load(".assets/NEw pack blood/1/1_20.png"),
        image.load(".assets/NEw pack blood/1/1_21.png"),
        image.load(".assets/NEw pack blood/1/1_22.png"),
        image.load(".assets/NEw pack blood/1/1_23.png"),
        image.load(".assets/NEw pack blood/1/1_24.png"),
        image.load(".assets/NEw pack blood/1/1_25.png"),
        image.load(".assets/NEw pack blood/1/1_26.png"),
        image.load(".assets/NEw pack blood/1/1_27.png"),
        image.load(".assets/NEw pack blood/1/1_28.png"),
        image.load(".assets/NEw pack blood/1/1_29.png"),
    ]
    Flyweight.data["start_button"] = [
        image.load(".assets/Simple UI Pack/Buttons/64x64/Start.png"),
        image.load(".assets/Simple UI Pack/Buttons/64x64/StartGray.png"),
        image.load(".assets/Simple UI Pack/Buttons/64x64/StartPressed.png"),
    ]
    Flyweight.data["exit_button"] = [
        image.load(".assets/Simple UI Pack/Buttons/64x64/Exit.png"),
        image.load(".assets/Simple UI Pack/Buttons/64x64/ExitGray.png"),
        image.load(".assets/Simple UI Pack/Buttons/64x64/ExitPressed.png"),
    ]
    Flyweight.data["coin"] = [
        image.load(".assets/Simple UI Pack/HUD/64x64/Coin_1.png"),
        image.load(".assets/Simple UI Pack/HUD/64x64/Coin_2.png"),
        image.load(".assets/Simple UI Pack/HUD/64x64/Coin_3.png"),
        image.load(".assets/Simple UI Pack/HUD/64x64/Coin_4.png"),
    ]
    Flyweight.data["confirm_button"] = [
        image.load(
            ".assets/Simple UI Pack/Icons and Vectors/64x64/Icons/Icon_Confirm1.png"
        ),
        image.load(
            ".assets/Simple UI Pack/Icons and Vectors/64x64/Icons/Icon_Confirm2.png"
        ),
    ]
    Flyweight.data["pause_button"] = [
        image.load(
            ".assets/Simple UI Pack/Icons and Vectors/64x64/Icons/Icon_Pause1Blue.png"
        ),
        image.load(
            ".assets/Simple UI Pack/Icons and Vectors/64x64/Icons/Icon_Pause2.png"
        ),
    ]
    Flyweight.data["sound_button"] = [
        image.load(
            ".assets/Simple UI Pack/Icons and Vectors/64x64/Icons/Icon_SoundMutedRed.png"
        ),
        image.load(
            ".assets/Simple UI Pack/Icons and Vectors/64x64/Icons/Icon_SoundOnGreen.png"
        ),
    ]
    Flyweight.data["star_button"] = [
        image.load(
            ".assets/Simple UI Pack/Icons and Vectors/64x64/Icons/Icon_Star.png"
        ),
        image.load(
            ".assets/Simple UI Pack/Icons and Vectors/64x64/Icons/Icon_StarEmpty.png"
        ),
    ]
    Flyweight.data["shop_button"] = [
        image.load(".assets/Simple UI Pack/Menu/64x64/Texts/Green/ShopGreen.png"),
        image.load(".assets/Simple UI Pack/Menu/64x64/Texts/Red/ShopRed.png"),
    ]
    Flyweight.data["you_button"] = [
        image.load(".assets/Simple UI Pack/Menu/64x64/Texts/Green/YouGreen.png"),
        image.load(".assets/Simple UI Pack/Menu/64x64/Texts/Red/YouRed.png"),
    ]


class NotAnimated(Flyweight):
    """
    This class is container for NotAnimated objects

    Keywords:
        "crosshair"
        "bg_mountain"
        "bg_moon"
        "bg_desert"
        "bg_rocks"
        "bg_peaks"
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
    """

    Flyweight.data["crosshair"] = image.load(
        ".assets/Crosshairs/Outline/CrosshairsOutline17.png"
    )
    Flyweight.data["bg_mountain"] = image.load(
        ".assets/Desolate Places/Cloudy Mountains.png"
    )
    Flyweight.data["bg_moon"] = image.load(".assets/Desolate Places/Dusty Moon.png")
    Flyweight.data["bg_desert"] = image.load(
        ".assets/Desolate Places/Hidden Desert.png"
    )
    Flyweight.data["bg_rocks"] = image.load(".assets/Desolate Places/Misty Rocks.png")
    Flyweight.data["bg_peaks"] = image.load(".assets/Desolate Places/Starry Peaks.png")
    Flyweight.data["icons_skill"] = [
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
    ]
    Flyweight.data["start_menu_sound"] = Sound(".assets/game_Sound/Spy/Spy.mp3")
    Flyweight.data["game_sound"] = [
        Sound(".assets/game_Sound/16_bit_space.ogg"),
        Sound(".assets/game_Sound/future.ogg"),
        Sound(".assets/game_Sound/glitch.ogg"),
        Sound(".assets/game_Sound/retro_metal.ogg"),
    ]
    Flyweight.data["hearth"] = [
        image.load(".assets/health/heart_1.png"),
        image.load(".assets/health/heart_2.png"),
        image.load(".assets/health/heart_3.png"),
    ]
    Flyweight.data["shield"] = [
        image.load(".assets/health/shield_1.png"),
        image.load(".assets/health/shield_2.png"),
        image.load(".assets/health/shield_3.png"),
    ]
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
    Flyweight.data["icon_template"] = image.load(
        ".assets/Simple UI Pack/Icons and Vectors/64x64/Icons/IconTemplate.png"
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
    Flyweight.data["elenore_menu_voices"] = [
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
    ]
    Flyweight.data["elenore_demaged_voices"] = [
        Sound(".assets/Elenore/Type 2/damaged1.wav"),
        Sound(".assets/Elenore/Type 2/damaged2.wav"),
        Sound(".assets/Elenore/Type 2/damaged3.wav"),
    ]
    Flyweight.data["elenore_healed_voices"] = [
        Sound(".assets/Elenore/Type 2/heal.wav"),
        Sound(".assets/Elenore/Type 2/healed1.wav"),
        Sound(".assets/Elenore/Type 2/healed2.wav"),
        Sound(".assets/Elenore/Type 2/healed3.wav"),
    ]
    Flyweight.data["elenore_shield_voices"] = Sound(".assets/Elenore/Type 2/cure.wav")
    Flyweight.data["moonpie_menu_voices"] = [
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
    ]
    Flyweight.data["moonpie_demaged_voices"] = [
        Sound(".assets/MoonPie/RPG Voice Starter Pack/Type 1/damaged1.wav"),
        Sound(".assets/MoonPie/RPG Voice Starter Pack/Type 1/damaged2.wav"),
        Sound(".assets/MoonPie/RPG Voice Starter Pack/Type 1/damaged3.wav"),
    ]
    Flyweight.data["moonpie_healed_voices"] = [
        Sound(".assets/MoonPie/RPG Voice Starter Pack/Type 1/heal.wav"),
        Sound(".assets/MoonPie/RPG Voice Starter Pack/Type 1/healed1.wav"),
        Sound(".assets/MoonPie/RPG Voice Starter Pack/Type 1/healed2.wav"),
        Sound(".assets/MoonPie/RPG Voice Starter Pack/Type 1/healed3.wav"),
    ]
    Flyweight.data["moonpie_shield_voices"] = Sound(
        ".assets/MoonPie/RPG Voice Starter Pack/Type 1/cure.wav"
    )
