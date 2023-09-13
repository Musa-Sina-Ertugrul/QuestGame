"""
    This file contains Flyweights as Prototype
    Flyweight class is an abstract class it has been
    inhereted by Animated and Not_Animated classes
    These two classes will contain assests as static

    TODO:NotAnimated class will be added
"""
from abc import ABC
from typing import Dict, List
import numpy as np
from pygame.image import load
from pygame.surface import Surface


class Flyweight(ABC):
    """
    Data container for Flyweight objects

    This class is an abstract class and is inhereted by Animeted
    and Not_Animated classes

    Attributes:
        data (Dict[str, List[Surface]]) : contains Surface objects
    """

    data: Dict[str, List[Surface]] = {}


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
    """

    on_animation = np.zeros(100, dtype=bool)  # 100 is maximum animated object count
    Flyweight.data["fire_cast"] = [  # use / instead of / if you are in windows !!!
        load(".assets/casts/fire_cast/FireCast_96x96_1.png"),
        load(".assets/casts/fire_cast/FireCast_96x96_2.png"),
        load(".assets/casts/fire_cast/FireCast_96x96_3.png"),
        load(".assets/casts/fire_cast/FireCast_96x96_4.png"),
        load(".assets/casts/fire_cast/FireCast_96x96_5.png"),
        load(".assets/casts/fire_cast/FireCast_96x96_6.png"),
        load(".assets/casts/fire_cast/FireCast_96x96_7.png"),
        load(".assets/casts/fire_cast/FireCast_96x96_8.png"),
        load(".assets/casts/fire_cast/FireCast_96x96_9.png"),
        load(".assets/casts/fire_cast/FireCast_96x96_10.png"),
        load(".assets/casts/fire_cast/FireCast_96x96_11.png"),
        load(".assets/casts/fire_cast/FireCast_96x96_12.png"),
        load(".assets/casts/fire_cast/FireCast_96x96_13.png"),
        load(".assets/casts/fire_cast/FireCast_96x96_14.png"),
        load(".assets/casts/fire_cast/FireCast_96x96_15.png"),
        load(".assets/casts/fire_cast/FireCast_96x96_16.png"),
        load(".assets/casts/fire_cast/FireCast_96x96_17.png"),
        load(".assets/casts/fire_cast/FireCast_96x96_18.png"),
        load(".assets/casts/fire_cast/FireCast_96x96_19.png"),
        load(".assets/casts/fire_cast/FireCast_96x96_20.png"),
        load(".assets/casts/fire_cast/FireCast_96x96_21.png"),
        load(".assets/casts/fire_cast/FireCast_96x96_22.png"),
        load(".assets/casts/fire_cast/FireCast_96x96_23.png"),
        load(".assets/casts/fire_cast/FireCast_96x96_24.png"),
        load(".assets/casts/fire_cast/FireCast_96x96_25.png"),
        load(".assets/casts/fire_cast/FireCast_96x96_26.png"),
        load(".assets/casts/fire_cast/FireCast_96x96_27.png"),
        load(".assets/casts/fire_cast/FireCast_96x96_28.png"),
    ]
    Flyweight.data["ice_cast"] = [
        load(".assets/casts/ice_shatter/IceShatter_96x96_1.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_2.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_3.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_4.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_5.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_6.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_7.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_8.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_9.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_10.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_11.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_12.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_13.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_14.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_15.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_16.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_17.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_18.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_19.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_20.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_21.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_22.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_23.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_24.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_25.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_26.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_27.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_28.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_29.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_30.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_31.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_32.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_33.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_34.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_35.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_36.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_37.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_38.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_39.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_40.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_41.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_42.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_43.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_44.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_45.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_46.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_47.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_48.png"),
        load(".assets/casts/ice_shatter/IceShatter_96x96_49.png"),
    ]
    Flyweight.data["light_cast"] = [
        load(".assets/casts/light_cast/LightCast_96_1.png"),
        load(".assets/casts/light_cast/LightCast_96_2.png"),
        load(".assets/casts/light_cast/LightCast_96_3.png"),
        load(".assets/casts/light_cast/LightCast_96_4.png"),
        load(".assets/casts/light_cast/LightCast_96_5.png"),
        load(".assets/casts/light_cast/LightCast_96_6.png"),
        load(".assets/casts/light_cast/LightCast_96_7.png"),
        load(".assets/casts/light_cast/LightCast_96_8.png"),
        load(".assets/casts/light_cast/LightCast_96_9.png"),
        load(".assets/casts/light_cast/LightCast_96_10.png"),
        load(".assets/casts/light_cast/LightCast_96_11.png"),
        load(".assets/casts/light_cast/LightCast_96_12.png"),
        load(".assets/casts/light_cast/LightCast_96_13.png"),
        load(".assets/casts/light_cast/LightCast_96_14.png"),
        load(".assets/casts/light_cast/LightCast_96_15.png"),
        load(".assets/casts/light_cast/LightCast_96_16.png"),
        load(".assets/casts/light_cast/LightCast_96_17.png"),
        load(".assets/casts/light_cast/LightCast_96_18.png"),
        load(".assets/casts/light_cast/LightCast_96_19.png"),
        load(".assets/casts/light_cast/LightCast_96_20.png"),
        load(".assets/casts/light_cast/LightCast_96_21.png"),
        load(".assets/casts/light_cast/LightCast_96_22.png"),
        load(".assets/casts/light_cast/LightCast_96_23.png"),
        load(".assets/casts/light_cast/LightCast_96_24.png"),
        load(".assets/casts/light_cast/LightCast_96_25.png"),
        load(".assets/casts/light_cast/LightCast_96_26.png"),
        load(".assets/casts/light_cast/LightCast_96_27.png"),
        load(".assets/casts/light_cast/LightCast_96_28.png"),
        load(".assets/casts/light_cast/LightCast_96_29.png"),
        load(".assets/casts/light_cast/LightCast_96_30.png"),
        load(".assets/casts/light_cast/LightCast_96_31.png"),
        load(".assets/casts/light_cast/LightCast_96_32.png"),
        load(".assets/casts/light_cast/LightCast_96_33.png"),
        load(".assets/casts/light_cast/LightCast_96_34.png"),
        load(".assets/casts/light_cast/LightCast_96_35.png"),
        load(".assets/casts/light_cast/LightCast_96_36.png"),
        load(".assets/casts/light_cast/LightCast_96_37.png"),
        load(".assets/casts/light_cast/LightCast_96_38.png"),
        load(".assets/casts/light_cast/LightCast_96_39.png"),
        load(".assets/casts/light_cast/LightCast_96_40.png"),
        load(".assets/casts/light_cast/LightCast_96_41.png"),
        load(".assets/casts/light_cast/LightCast_96_42.png"),
        load(".assets/casts/light_cast/LightCast_96_43.png"),
        load(".assets/casts/light_cast/LightCast_96_44.png"),
        load(".assets/casts/light_cast/LightCast_96_45.png"),
        load(".assets/casts/light_cast/LightCast_96_46.png"),
        load(".assets/casts/light_cast/LightCast_96_47.png"),
        load(".assets/casts/light_cast/LightCast_96_48.png"),
    ]
    Flyweight.data["magic_cast"] = [
        load(".assets/casts/magic_barrier/MagicBarrier_64x64_1.png"),
        load(".assets/casts/magic_barrier/MagicBarrier_64x64_2.png"),
        load(".assets/casts/magic_barrier/MagicBarrier_64x64_3.png"),
        load(".assets/casts/magic_barrier/MagicBarrier_64x64_4.png"),
        load(".assets/casts/magic_barrier/MagicBarrier_64x64_5.png"),
        load(".assets/casts/magic_barrier/MagicBarrier_64x64_6.png"),
        load(".assets/casts/magic_barrier/MagicBarrier_64x64_7.png"),
        load(".assets/casts/magic_barrier/MagicBarrier_64x64_8.png"),
        load(".assets/casts/magic_barrier/MagicBarrier_64x64_9.png"),
        load(".assets/casts/magic_barrier/MagicBarrier_64x64_10.png"),
        load(".assets/casts/magic_barrier/MagicBarrier_64x64_11.png"),
        load(".assets/casts/magic_barrier/MagicBarrier_64x64_12.png"),
        load(".assets/casts/magic_barrier/MagicBarrier_64x64_13.png"),
        load(".assets/casts/magic_barrier/MagicBarrier_64x64_14.png"),
        load(".assets/casts/magic_barrier/MagicBarrier_64x64_15.png"),
        load(".assets/casts/magic_barrier/MagicBarrier_64x64_16.png"),
        load(".assets/casts/magic_barrier/MagicBarrier_64x64_17.png"),
        load(".assets/casts/magic_barrier/MagicBarrier_64x64_18.png"),
        load(".assets/casts/magic_barrier/MagicBarrier_64x64_19.png"),
        load(".assets/casts/magic_barrier/MagicBarrier_64x64_20.png"),
        load(".assets/casts/magic_barrier/MagicBarrier_64x64_21.png"),
        load(".assets/casts/magic_barrier/MagicBarrier_64x64_21.png"),
        load(".assets/casts/magic_barrier/MagicBarrier_64x64_22.png"),
        load(".assets/casts/magic_barrier/MagicBarrier_64x64_23.png"),
        load(".assets/casts/magic_barrier/MagicBarrier_64x64_24.png"),
        load(".assets/casts/magic_barrier/MagicBarrier_64x64_25.png"),
        load(".assets/casts/magic_barrier/MagicBarrier_64x64_26.png"),
        load(".assets/casts/magic_barrier/MagicBarrier_64x64_27.png"),
        load(".assets/casts/magic_barrier/MagicBarrier_64x64_28.png"),
        load(".assets/casts/magic_barrier/MagicBarrier_64x64_29.png"),
        load(".assets/casts/magic_barrier/MagicBarrier_64x64_30.png"),
        load(".assets/casts/magic_barrier/MagicBarrier_64x64_31.png"),
        load(".assets/casts/magic_barrier/MagicBarrier_64x64_32.png"),
        load(".assets/casts/magic_barrier/MagicBarrier_64x64_33.png"),
    ]
    Flyweight.data["crazy_chest"] = [
        load(".assets/chests/crazy/Layer-1.png"),
        load(".assets/chests/crazy/Layer-2.png"),
        load(".assets/chests/crazy/Layer-3.png"),
        load(".assets/chests/crazy/Layer-4.png"),
        load(".assets/chests/crazy/Layer-5.png"),
        load(".assets/chests/crazy/Layer-6.png"),
        load(".assets/chests/crazy/Layer-7.png"),
        load(".assets/chests/crazy/Layer-8.png"),
    ]
    Flyweight.data["gold_chest"] = [
        load(".assets/chests/gold/Layer-1.png"),
        load(".assets/chests/gold/Layer-2.png"),
        load(".assets/chests/gold/Layer-3.png"),
        load(".assets/chests/gold/Layer-4.png"),
        load(".assets/chests/gold/Layer-5.png"),
        load(".assets/chests/gold/Layer-6.png"),
        load(".assets/chests/gold/Layer-7.png"),
        load(".assets/chests/gold/Layer-8.png"),
    ]
    Flyweight.data["king_chest"] = [
        load(".assets/chests/KING/Layer-1.png"),
        load(".assets/chests/KING/Layer-2.png"),
        load(".assets/chests/KING/Layer-3.png"),
        load(".assets/chests/KING/Layer-4.png"),
        load(".assets/chests/KING/Layer-5.png"),
        load(".assets/chests/KING/Layer-6.png"),
        load(".assets/chests/KING/Layer-7.png"),
        load(".assets/chests/KING/Layer-8.png"),
    ]
    Flyweight.data["silver_chest"] = [
        load(".assets/chests/Silver/Layer-1.png"),
        load(".assets/chests/Silver/Layer-2.png"),
        load(".assets/chests/Silver/Layer-3.png"),
        load(".assets/chests/Silver/Layer-4.png"),
        load(".assets/chests/Silver/Layer-5.png"),
        load(".assets/chests/Silver/Layer-6.png"),
        load(".assets/chests/Silver/Layer-7.png"),
        load(".assets/chests/Silver/Layer-8.png"),
    ]
    Flyweight.data["dark_spell_1"] = [
        load(
            ".assets/Dark VFX 01 - 02/Dark VFX 1/Separeted frames/Dark VFX 1 (40x32)1.png"
        ),
        load(
            ".assets/Dark VFX 01 - 02/Dark VFX 1/Separeted frames/Dark VFX 1 (40x32)2.png"
        ),
        load(
            ".assets/Dark VFX 01 - 02/Dark VFX 1/Separeted frames/Dark VFX 1 (40x32)3.png"
        ),
        load(
            ".assets/Dark VFX 01 - 02/Dark VFX 1/Separeted frames/Dark VFX 1 (40x32)4.png"
        ),
        load(
            ".assets/Dark VFX 01 - 02/Dark VFX 1/Separeted frames/Dark VFX 1 (40x32)5.png"
        ),
        load(
            ".assets/Dark VFX 01 - 02/Dark VFX 1/Separeted frames/Dark VFX 1 (40x32)6.png"
        ),
        load(
            ".assets/Dark VFX 01 - 02/Dark VFX 1/Separeted frames/Dark VFX 1 (40x32)7.png"
        ),
        load(
            ".assets/Dark VFX 01 - 02/Dark VFX 1/Separeted frames/Dark VFX 1 (40x32)8.png"
        ),
        load(
            ".assets/Dark VFX 01 - 02/Dark VFX 1/Separeted frames/Dark VFX 1 (40x32)9.png"
        ),
        load(
            ".assets/Dark VFX 01 - 02/Dark VFX 1/Separeted frames/Dark VFX 1 (40x32)10.png"
        ),
        load(
            ".assets/Dark VFX 01 - 02/Dark VFX 1/Separeted frames/Dark VFX 1 (40x32)11.png"
        ),
        load(
            ".assets/Dark VFX 01 - 02/Dark VFX 1/Separeted frames/Dark VFX 1 (40x32)12.png"
        ),
        load(
            ".assets/Dark VFX 01 - 02/Dark VFX 1/Separeted frames/Dark VFX 1 (40x32)13.png"
        ),
        load(
            ".assets/Dark VFX 01 - 02/Dark VFX 1/Separeted frames/Dark VFX 1 (40x32)14.png"
        ),
        load(
            ".assets/Dark VFX 01 - 02/Dark VFX 1/Separeted frames/Dark VFX 1 (40x32)15.png"
        ),
        load(
            ".assets/Dark VFX 01 - 02/Dark VFX 1/Separeted frames/Dark VFX 1 (40x32)16.png"
        ),
        load(
            ".assets/Dark VFX 01 - 02/Dark VFX 1/Separeted frames/Dark VFX 1 (40x32)17.png"
        ),
    ]
    Flyweight.data["dark_spell_2"] = [
        load(
            ".assets/Dark VFX 01 - 02/Dark VFX 2/Separated Frames/Dark VFX 2 (48x64)1.png"
        ),
        load(
            ".assets/Dark VFX 01 - 02/Dark VFX 2/Separated Frames/Dark VFX 2 (48x64)2.png"
        ),
        load(
            ".assets/Dark VFX 01 - 02/Dark VFX 2/Separated Frames/Dark VFX 2 (48x64)3.png"
        ),
        load(
            ".assets/Dark VFX 01 - 02/Dark VFX 2/Separated Frames/Dark VFX 2 (48x64)4.png"
        ),
        load(
            ".assets/Dark VFX 01 - 02/Dark VFX 2/Separated Frames/Dark VFX 2 (48x64)5.png"
        ),
        load(
            ".assets/Dark VFX 01 - 02/Dark VFX 2/Separated Frames/Dark VFX 2 (48x64)6.png"
        ),
        load(
            ".assets/Dark VFX 01 - 02/Dark VFX 2/Separated Frames/Dark VFX 2 (48x64)7.png"
        ),
        load(
            ".assets/Dark VFX 01 - 02/Dark VFX 2/Separated Frames/Dark VFX 2 (48x64)8.png"
        ),
        load(
            ".assets/Dark VFX 01 - 02/Dark VFX 2/Separated Frames/Dark VFX 2 (48x64)9.png"
        ),
        load(
            ".assets/Dark VFX 01 - 02/Dark VFX 2/Separated Frames/Dark VFX 2 (48x64)10.png"
        ),
        load(
            ".assets/Dark VFX 01 - 02/Dark VFX 2/Separated Frames/Dark VFX 2 (48x64)11.png"
        ),
        load(
            ".assets/Dark VFX 01 - 02/Dark VFX 2/Separated Frames/Dark VFX 2 (48x64)12.png"
        ),
        load(
            ".assets/Dark VFX 01 - 02/Dark VFX 2/Separated Frames/Dark VFX 2 (48x64)13.png"
        ),
        load(
            ".assets/Dark VFX 01 - 02/Dark VFX 2/Separated Frames/Dark VFX 2 (48x64)14.png"
        ),
        load(
            ".assets/Dark VFX 01 - 02/Dark VFX 2/Separated Frames/Dark VFX 2 (48x64)15.png"
        ),
        load(
            ".assets/Dark VFX 01 - 02/Dark VFX 2/Separated Frames/Dark VFX 2 (48x64)16.png"
        ),
    ]
    Flyweight.data["elenore"] = [
        load(".assets/Elenore/Idle/Idle1.png"),
        load(".assets/Elenore/Idle/Idle2.png"),
        load(".assets/Elenore/Idle/Idle3.png"),
        load(".assets/Elenore/Idle/Idle4.png"),
        load(".assets/Elenore/Idle/Idle5.png"),
        load(".assets/Elenore/Idle/Idle6.png"),
        load(".assets/Elenore/Idle/Idle7.png"),
        load(".assets/Elenore/Idle/Idle8.png"),
        load(".assets/Elenore/Idle/Idle9.png"),
    ]
    Flyweight.data["elenore_shadow"] = [
        load(".assets/Elenore/Idle/Shadow/Shadow1.png"),
        load(".assets/Elenore/Idle/Shadow/Shadow2.png"),
        load(".assets/Elenore/Idle/Shadow/Shadow3.png"),
        load(".assets/Elenore/Idle/Shadow/Shadow4.png"),
        load(".assets/Elenore/Idle/Shadow/Shadow5.png"),
        load(".assets/Elenore/Idle/Shadow/Shadow6.png"),
        load(".assets/Elenore/Idle/Shadow/Shadow7.png"),
        load(".assets/Elenore/Idle/Shadow/Shadow8.png"),
        load(".assets/Elenore/Idle/Shadow/Shadow9.png"),
    ]
    Flyweight.data["eye_fire_blue"] = [
        load(".assets/enemies/Eye Fire Blue/eye fire blue1.png"),
        load(".assets/enemies/Eye Fire Blue/eye fire blue2.png"),
        load(".assets/enemies/Eye Fire Blue/eye fire blue3.png"),
        load(".assets/enemies/Eye Fire Blue/eye fire blue4.png"),
        load(".assets/enemies/Eye Fire Blue/eye fire blue5.png"),
        load(".assets/enemies/Eye Fire Blue/eye fire blue6.png"),
        load(".assets/enemies/Eye Fire Blue/eye fire blue7.png"),
    ]
    Flyweight.data["eye_fire_red"] = [
        load(".assets/enemies/Eye Fire Red/eye fire1.png"),
        load(".assets/enemies/Eye Fire Red/eye fire2.png"),
        load(".assets/enemies/Eye Fire Red/eye fire3.png"),
        load(".assets/enemies/Eye Fire Red/eye fire4.png"),
        load(".assets/enemies/Eye Fire Red/eye fire5.png"),
        load(".assets/enemies/Eye Fire Red/eye fire6.png"),
        load(".assets/enemies/Eye Fire Red/eye fire7.png"),
    ]
    Flyweight.data["bat"] = [
        load(".assets/enemies/sprites/Bat/bat1.png"),
        load(".assets/enemies/sprites/Bat/bat2.png"),
        load(".assets/enemies/sprites/Bat/bat3.png"),
        load(".assets/enemies/sprites/Bat/bat4.png"),
        load(".assets/enemies/sprites/Bat/bat5.png"),
    ]
    Flyweight.data["ghost"] = [
        load(".assets/enemies/sprites/Ghost/ghost1.png"),
        load(".assets/enemies/sprites/Ghost/ghost2.png"),
        load(".assets/enemies/sprites/Ghost/ghost3.png"),
        load(".assets/enemies/sprites/Ghost/ghost4.png"),
        load(".assets/enemies/sprites/Ghost/ghost5.png"),
    ]
    Flyweight.data["lizard"] = [
        load(".assets/enemies/sprites/lizard moves/lizard-move1.png"),
        load(".assets/enemies/sprites/lizard moves/lizard-move2.png"),
        load(".assets/enemies/sprites/lizard moves/lizard-move3.png"),
    ]
    Flyweight.data["skeleton"] = [
        load(".assets/enemies/sprites/Skeleton-Walk/skeleton-walk1.png"),
        load(".assets/enemies/sprites/Skeleton-Walk/skeleton-walk2.png"),
        load(".assets/enemies/sprites/Skeleton-Walk/skeleton-walk3.png"),
        load(".assets/enemies/sprites/Skeleton-Walk/skeleton-walk4.png"),
        load(".assets/enemies/sprites/Skeleton-Walk/skeleton-walk5.png"),
        load(".assets/enemies/sprites/Skeleton-Walk/skeleton-walk6.png"),
        load(".assets/enemies/sprites/Skeleton-Walk/skeleton-walk7.png"),
        load(".assets/enemies/sprites/Skeleton-Walk/skeleton-walk8.png"),
    ]
    Flyweight.data["slime"] = [
        load(".assets/enemies/sprites/Slime/slime1.png"),
        load(".assets/enemies/sprites/Slime/slime2.png"),
        load(".assets/enemies/sprites/Slime/slime3.png"),
        load(".assets/enemies/sprites/Slime/slime4.png"),
        load(".assets/enemies/sprites/Slime/slime5.png"),
    ]
    Flyweight.data["crab"] = [
        load(".assets/enemies/sprites/Walk/crab-walk1.png"),
        load(".assets/enemies/sprites/Walk/crab-walk2.png"),
        load(".assets/enemies/sprites/Walk/crab-walk3.png"),
        load(".assets/enemies/sprites/Walk/crab-walk4.png"),
        load(".assets/enemies/sprites/Walk/crab-walk5.png"),
        load(".assets/enemies/sprites/Walk/crab-walk6.png"),
    ]
    Flyweight.data["ice_spell_1_hit"] = [
        load(".assets/Ice Effect 01/Ice VFX 1/Separated Frames/VFX 1 Hit1.png"),
        load(".assets/Ice Effect 01/Ice VFX 1/Separated Frames/VFX 1 Hit2.png"),
        load(".assets/Ice Effect 01/Ice VFX 1/Separated Frames/VFX 1 Hit3.png"),
        load(".assets/Ice Effect 01/Ice VFX 1/Separated Frames/VFX 1 Hit4.png"),
        load(".assets/Ice Effect 01/Ice VFX 1/Separated Frames/VFX 1 Hit5.png"),
        load(".assets/Ice Effect 01/Ice VFX 1/Separated Frames/VFX 1 Hit6.png"),
        load(".assets/Ice Effect 01/Ice VFX 1/Separated Frames/VFX 1 Hit7.png"),
        load(".assets/Ice Effect 01/Ice VFX 1/Separated Frames/VFX 1 Hit8.png"),
    ]
    Flyweight.data["ice_spell_1_move"] = [
        load(".assets/Ice Effect 01/Ice VFX 1/Separated Frames/VFX 1 Repeatable1.png"),
        load(".assets/Ice Effect 01/Ice VFX 1/Separated Frames/VFX 1 Repeatable2.png"),
        load(".assets/Ice Effect 01/Ice VFX 1/Separated Frames/VFX 1 Repeatable3.png"),
        load(".assets/Ice Effect 01/Ice VFX 1/Separated Frames/VFX 1 Repeatable4.png"),
        load(".assets/Ice Effect 01/Ice VFX 1/Separated Frames/VFX 1 Repeatable5.png"),
        load(".assets/Ice Effect 01/Ice VFX 1/Separated Frames/VFX 1 Repeatable6.png"),
        load(".assets/Ice Effect 01/Ice VFX 1/Separated Frames/VFX 1 Repeatable7.png"),
        load(".assets/Ice Effect 01/Ice VFX 1/Separated Frames/VFX 1 Repeatable8.png"),
        load(".assets/Ice Effect 01/Ice VFX 1/Separated Frames/VFX 1 Repeatable9.png"),
        load(".assets/Ice Effect 01/Ice VFX 1/Separated Frames/VFX 1 Repeatable10.png"),
    ]
    Flyweight.data["ice_spell_1_strat"] = [
        load(".assets/Ice Effect 01/Ice VFX 1/Separated Frames/VFX 1 Start1.png"),
        load(".assets/Ice Effect 01/Ice VFX 1/Separated Frames/VFX 1 Start2.png"),
        load(".assets/Ice Effect 01/Ice VFX 1/Separated Frames/VFX 1 Start3.png"),
    ]
    Flyweight.data["ice_spell_2_active"] = [
        load(".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Active1.png"),
        load(".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Active2.png"),
        load(".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Active3.png"),
        load(".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Active4.png"),
        load(".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Active5.png"),
        load(".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Active6.png"),
        load(".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Active7.png"),
        load(".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Active8.png"),
        load(".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Active9.png"),
    ]
    Flyweight.data["ice_spell_2_ending"] = [
        load(".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Ending1.png"),
        load(".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Ending2.png"),
        load(".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Ending3.png"),
        load(".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Ending4.png"),
        load(".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Ending5.png"),
        load(".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Ending6.png"),
        load(".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Ending7.png"),
        load(".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Ending8.png"),
        load(".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Ending9.png"),
        load(".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Ending11.png"),
        load(".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Ending12.png"),
        load(".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Ending13.png"),
        load(".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Ending14.png"),
        load(".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Ending15.png"),
        load(".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Ending16.png"),
        load(".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Ending17.png"),
        load(".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Ending18.png"),
    ]
    Flyweight.data["ice_spell_2_start"] = [
        load(".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Start1.png"),
        load(".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Start2.png"),
        load(".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Start3.png"),
        load(".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Start4.png"),
        load(".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Start5.png"),
        load(".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Start6.png"),
        load(".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Start7.png"),
        load(".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Start8.png"),
        load(".assets/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Start9.png"),
    ]
    Flyweight.data["npc_ranger"] = [
        load(
            ".assets/Lively_NPCs_v3.0/individual sprites/elementals/leaf_ranger/leaf_ranger_1.png"
        ),
        load(
            ".assets/Lively_NPCs_v3.0/individual sprites/elementals/leaf_ranger/leaf_ranger_2.png"
        ),
        load(
            ".assets/Lively_NPCs_v3.0/individual sprites/elementals/leaf_ranger/leaf_ranger_3.png"
        ),
        load(
            ".assets/Lively_NPCs_v3.0/individual sprites/elementals/leaf_ranger/leaf_ranger_4.png"
        ),
    ]
    Flyweight.data["npc_gunslinger"] = [
        load(
            ".assets/Lively_NPCs_v3.0/individual sprites/steampunk/gunslinger/gunslinger_1.png"
        ),
        load(
            ".assets/Lively_NPCs_v3.0/individual sprites/steampunk/gunslinger/gunslinger_2.png"
        ),
        load(
            ".assets/Lively_NPCs_v3.0/individual sprites/steampunk/gunslinger/gunslinger_3.png"
        ),
        load(
            ".assets/Lively_NPCs_v3.0/individual sprites/steampunk/gunslinger/gunslinger_4.png"
        ),
        load(
            ".assets/Lively_NPCs_v3.0/individual sprites/steampunk/gunslinger/gunslinger_5.png"
        ),
    ]
    Flyweight.data["npc_witch"] = [
        load(".assets/Lively_NPCs_v3.0/individual sprites/medieval/witch/witch_00.png"),
        load(".assets/Lively_NPCs_v3.0/individual sprites/medieval/witch/witch_01.png"),
        load(".assets/Lively_NPCs_v3.0/individual sprites/medieval/witch/witch_02.png"),
        load(".assets/Lively_NPCs_v3.0/individual sprites/medieval/witch/witch_03.png"),
        load(".assets/Lively_NPCs_v3.0/individual sprites/medieval/witch/witch_04.png"),
    ]
    Flyweight.data["npc_king"] = [
        load(".assets/Lively_NPCs_v3.0/individual sprites/medieval/king/king_00.png"),
        load(".assets/Lively_NPCs_v3.0/individual sprites/medieval/king/king_01.png"),
        load(".assets/Lively_NPCs_v3.0/individual sprites/medieval/king/king_02.png"),
        load(".assets/Lively_NPCs_v3.0/individual sprites/medieval/king/king_03.png"),
        load(".assets/Lively_NPCs_v3.0/individual sprites/medieval/king/king_04.png"),
    ]
    Flyweight.data["npc_monk"] = [
        load(
            ".assets/Lively_NPCs_v3.0/individual sprites/elementals/ground_monk/ground_monk_1.png"
        ),
        load(
            ".assets/Lively_NPCs_v3.0/individual sprites/elementals/ground_monk/ground_monk_2.png"
        ),
        load(
            ".assets/Lively_NPCs_v3.0/individual sprites/elementals/ground_monk/ground_monk_3.png"
        ),
        load(
            ".assets/Lively_NPCs_v3.0/individual sprites/elementals/ground_monk/ground_monk_4.png"
        ),
    ]
    Flyweight.data["npc_trader"] = [
        load(
            ".assets/Lively_NPCs_v3.0/individual sprites/steampunk/trader/trader_1.png"
        ),
        load(
            ".assets/Lively_NPCs_v3.0/individual sprites/steampunk/trader/trader_2.png"
        ),
        load(
            ".assets/Lively_NPCs_v3.0/individual sprites/steampunk/trader/trader_3.png"
        ),
        load(
            ".assets/Lively_NPCs_v3.0/individual sprites/steampunk/trader/trader_4.png"
        ),
    ]
    Flyweight.data["npc_fairy"] = [
        load(".assets/Lively_NPCs_v3.0/individual sprites/medieval/fairy/fairy_1.png"),
        load(".assets/Lively_NPCs_v3.0/individual sprites/medieval/fairy/fairy_2.png"),
        load(".assets/Lively_NPCs_v3.0/individual sprites/medieval/fairy/fairy_3.png"),
        load(".assets/Lively_NPCs_v3.0/individual sprites/medieval/fairy/fairy_4.png"),
    ]
    Flyweight.data["moonpie_front_idle"] = [
        load(".assets/MoonPie/girl_frames1.png"),
        load(".assets/MoonPie/girl_frames2.png"),
        load(".assets/MoonPie/girl_frames3.png"),
        load(".assets/MoonPie/girl_frames4.png"),
    ]
    Flyweight.data["moonpie_left_idle"] = [
        load(".assets/MoonPie/girl_frames5.png"),
        load(".assets/MoonPie/girl_frames6.png"),
        load(".assets/MoonPie/girl_frames7.png"),
        load(".assets/MoonPie/girl_frames8.png"),
    ]
    Flyweight.data["moonpie_right_idle"] = [
        load(".assets/MoonPie/girl_frames9.png"),
        load(".assets/MoonPie/girl_frames10.png"),
        load(".assets/MoonPie/girl_frames11.png"),
        load(".assets/MoonPie/girl_frames12.png"),
    ]
    Flyweight.data["moonpie_back_idle"] = [
        load(".assets/MoonPie/girl_frames13.png"),
        load(".assets/MoonPie/girl_frames14.png"),
        load(".assets/MoonPie/girl_frames15.png"),
        load(".assets/MoonPie/girl_frames16.png"),
    ]
    Flyweight.data["moonpie_front_run"] = [
        load(".assets/MoonPie/girl_frames17.png"),
        load(".assets/MoonPie/girl_frames18.png"),
        load(".assets/MoonPie/girl_frames19.png"),
        load(".assets/MoonPie/girl_frames20.png"),
        load(".assets/MoonPie/girl_frames21.png"),
        load(".assets/MoonPie/girl_frames22.png"),
    ]
    Flyweight.data["moonpie_left_run"] = [
        load(".assets/MoonPie/girl_frames23.png"),
        load(".assets/MoonPie/girl_frames24.png"),
        load(".assets/MoonPie/girl_frames25.png"),
        load(".assets/MoonPie/girl_frames26.png"),
        load(".assets/MoonPie/girl_frames27.png"),
        load(".assets/MoonPie/girl_frames28.png"),
    ]
    Flyweight.data["moonpie_right_run"] = [
        load(".assets/MoonPie/girl_frames29.png"),
        load(".assets/MoonPie/girl_frames30.png"),
        load(".assets/MoonPie/girl_frames31.png"),
        load(".assets/MoonPie/girl_frames32.png"),
        load(".assets/MoonPie/girl_frames33.png"),
        load(".assets/MoonPie/girl_frames34.png"),
    ]
    Flyweight.data["moonpie_back_run"] = [
        load(".assets/MoonPie/girl_frames35.png"),
        load(".assets/MoonPie/girl_frames36.png"),
        load(".assets/MoonPie/girl_frames37.png"),
        load(".assets/MoonPie/girl_frames38.png"),
        load(".assets/MoonPie/girl_frames39.png"),
        load(".assets/MoonPie/girl_frames40.png"),
    ]
    Flyweight.data["moonpie_death"] = [
        load(".assets/MoonPie/girl_frames41.png"),
        load(".assets/MoonPie/girl_frames42.png"),
        load(".assets/MoonPie/girl_frames43.png"),
        load(".assets/MoonPie/girl_frames44.png"),
    ]
    Flyweight.data["blood"] = [
        load(".assets/NEw pack blood/1/1_0.png"),
        load(".assets/NEw pack blood/1/1_1.png"),
        load(".assets/NEw pack blood/1/1_2.png"),
        load(".assets/NEw pack blood/1/1_3.png"),
        load(".assets/NEw pack blood/1/1_4.png"),
        load(".assets/NEw pack blood/1/1_5.png"),
        load(".assets/NEw pack blood/1/1_6.png"),
        load(".assets/NEw pack blood/1/1_7.png"),
        load(".assets/NEw pack blood/1/1_8.png"),
        load(".assets/NEw pack blood/1/1_9.png"),
        load(".assets/NEw pack blood/1/1_10.png"),
        load(".assets/NEw pack blood/1/1_11.png"),
        load(".assets/NEw pack blood/1/1_12.png"),
        load(".assets/NEw pack blood/1/1_13.png"),
        load(".assets/NEw pack blood/1/1_14.png"),
        load(".assets/NEw pack blood/1/1_15.png"),
        load(".assets/NEw pack blood/1/1_16.png"),
        load(".assets/NEw pack blood/1/1_17.png"),
        load(".assets/NEw pack blood/1/1_18.png"),
        load(".assets/NEw pack blood/1/1_19.png"),
        load(".assets/NEw pack blood/1/1_20.png"),
        load(".assets/NEw pack blood/1/1_21.png"),
        load(".assets/NEw pack blood/1/1_22.png"),
        load(".assets/NEw pack blood/1/1_23.png"),
        load(".assets/NEw pack blood/1/1_24.png"),
        load(".assets/NEw pack blood/1/1_25.png"),
        load(".assets/NEw pack blood/1/1_26.png"),
        load(".assets/NEw pack blood/1/1_27.png"),
        load(".assets/NEw pack blood/1/1_28.png"),
        load(".assets/NEw pack blood/1/1_29.png"),
    ]
    Flyweight.data["start_button"] = [
        load(".assets/Simple UI Pack/Buttons/64x64/Start.png"),
        load(".assets/Simple UI Pack/Buttons/64x64/StartGray.png"),
        load(".assets/Simple UI Pack/Buttons/64x64/StartPressed.png"),
    ]
    Flyweight.data["exit_button"] = [
        load(".assets/Simple UI Pack/Buttons/64x64/Exit.png"),
        load(".assets/Simple UI Pack/Buttons/64x64/ExitGray.png"),
        load(".assets/Simple UI Pack/Buttons/64x64/ExitPressed.png"),
    ]
    Flyweight.data["coin"] = [
        load(".assets/Simple UI Pack/HUD/64x64/Coin_1.png"),
        load(".assets/Simple UI Pack/HUD/64x64/Coin_2.png"),
        load(".assets/Simple UI Pack/HUD/64x64/Coin_3.png"),
        load(".assets/Simple UI Pack/HUD/64x64/Coin_4.png"),
    ]
