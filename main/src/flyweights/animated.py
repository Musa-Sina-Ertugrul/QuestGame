"""
This module contains Animated flyweight class

"""
from pygame import image

from .flyweight import Flyweight


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
        "reaper"
        "skeleton_big_idle"
        "skeleton_big_attack"
        "skeleton_big_hit"
        "skeleton_big_walk"
        "skeleton_big_death"
        "bringer_of_death_attack"
        "bringer_of_death_cast"
        "bringer_of_death_death"
        "bringer_of_death_hurt"
        "bringer_of_death_idle"
        "bringer_of_death_spell"
        "bringer_of_death_walk"
        "boss_demon_idle"
        "boss_demon_walk"
        "boss_demon_cleave"
        "boss_demon_hit"
        "boss_demon_death"
        "boss_frost_attack"
        "boss_frost_death"
        "boss_frost_idle"
        "boss_frost_hit"
        "boss_frost_walk"
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
    Flyweight.data["reaper"] = [
        image.load(".assets/enemies/reaper/PassiveRunningReaper_1.png"),
        image.load(".assets/enemies/reaper/PassiveRunningReaper_2.png"),
        image.load(".assets/enemies/reaper/PassiveRunningReaper_3.png"),
        image.load(".assets/enemies/reaper/PassiveRunningReaper_4.png"),
        image.load(".assets/enemies/reaper/PassiveRunningReaper_5.png"),
        image.load(".assets/enemies/reaper/PassiveRunningReaper_6.png"),
        image.load(".assets/enemies/reaper/PassiveRunningReaper_7.png"),
        image.load(".assets/enemies/reaper/PassiveRunningReaper_8.png"),
    ]
    Flyweight.data["skeleton_big_idle"] = [
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_1.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_2.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_3.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_4.png"),
    ]
    Flyweight.data["skeleton_big_attack"] = [
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_5.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_6.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_7.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_8.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_9.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_10.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_11.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_12.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_13.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_14.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_15.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_16.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_17.png"),
    ]
    Flyweight.data["skeleton_big_hit"] = [
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_18.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_19.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_20.png"),
    ]
    Flyweight.data["skeleton_big_walk"] = [
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_21.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_22.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_23.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_24.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_25.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_26.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_27.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_28.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_29.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_30.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_31.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_32.png"),
    ]
    Flyweight.data["skeleton_big_death"] = [
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_33.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_34.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_35.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_36.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_37.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_38.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_39.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_40.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_41.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_42.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_43.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_44.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_45.png"),
    ]
    Flyweight.data["skeleton_big_attack"] = [
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_21.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_22.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_23.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_24.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_25.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_26.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_27.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_28.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_29.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_30.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_31.png"),
        image.load(".assets/enemies/SkeletonBi/SkeletonBig_32.png"),
    ]
    Flyweight.data["bringer_of_death_attack"] = [
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Attack/Bringer-of-Death_Attack_1.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Attack/Bringer-of-Death_Attack_2.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Attack/Bringer-of-Death_Attack_3.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Attack/Bringer-of-Death_Attack_4.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Attack/Bringer-of-Death_Attack_5.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Attack/Bringer-of-Death_Attack_6.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Attack/Bringer-of-Death_Attack_7.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Attack/Bringer-of-Death_Attack_8.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Attack/Bringer-of-Death_Attack_9.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Attack/Bringer-of-Death_Attack_10.png"
        ),
    ]
    Flyweight.data["bringer_of_death_cast"] = [
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Cast/Bringer-of-Death_Cast_1.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Cast/Bringer-of-Death_Cast_2.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Cast/Bringer-of-Death_Cast_3.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Cast/Bringer-of-Death_Cast_4.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Cast/Bringer-of-Death_Cast_5.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Cast/Bringer-of-Death_Cast_6.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Cast/Bringer-of-Death_Cast_7.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Cast/Bringer-of-Death_Cast_8.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Cast/Bringer-of-Death_Cast_9.png"
        ),
    ]
    Flyweight.data["bringer_of_death_death"] = [
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Death/Bringer-of-Death_Death_1.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Death/Bringer-of-Death_Death_2.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Death/Bringer-of-Death_Death_3.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Death/Bringer-of-Death_Death_4.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Death/Bringer-of-Death_Death_5.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Death/Bringer-of-Death_Death_6.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Death/Bringer-of-Death_Death_7.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Death/Bringer-of-Death_Death_8.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Death/Bringer-of-Death_Death_9.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Death/Bringer-of-Death_Death_10.png"
        ),
    ]
    Flyweight.data["bringer_of_death_hurt"] = [
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Hurt/Bringer-of-Death_Hurt_1.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Hurt/Bringer-of-Death_Hurt_2.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Hurt/Bringer-of-Death_Hurt_3.png"
        ),
    ]
    Flyweight.data["bringer_of_death_idle"] = [
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Idle/Bringer-of-Death_Idle_1.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Idle/Bringer-of-Death_Idle_2.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Idle/Bringer-of-Death_Idle_3.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Idle/Bringer-of-Death_Idle_4.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Idle/Bringer-of-Death_Idle_5.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Idle/Bringer-of-Death_Idle_6.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Idle/Bringer-of-Death_Idle_7.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Idle/Bringer-of-Death_Idle_8.png"
        ),
    ]
    Flyweight.data["bringer_of_death_spell"] = [
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Spell/Bringer-of-Death_Spell_1.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Spell/Bringer-of-Death_Spell_2.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Spell/Bringer-of-Death_Spell_3.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Spell/Bringer-of-Death_Spell_4.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Spell/Bringer-of-Death_Spell_5.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Spell/Bringer-of-Death_Spell_6.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Spell/Bringer-of-Death_Spell_7.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Spell/Bringer-of-Death_Spell_8.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Spell/Bringer-of-Death_Spell_9.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Spell/Bringer-of-Death_Spell_10.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Spell/Bringer-of-Death_Spell_11.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Spell/Bringer-of-Death_Spell_12.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Spell/Bringer-of-Death_Spell_13.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Spell/Bringer-of-Death_Spell_14.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Spell/Bringer-of-Death_Spell_15.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Spell/Bringer-of-Death_Spell_16.png"
        ),
    ]
    Flyweight.data["bringer_of_death_walk"] = [
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Walk/Bringer-of-Death_Walk_1.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Walk/Bringer-of-Death_Walk_2.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Walk/Bringer-of-Death_Walk_3.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Walk/Bringer-of-Death_Walk_4.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Walk/Bringer-of-Death_Walk_5.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Walk/Bringer-of-Death_Walk_6.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Walk/Bringer-of-Death_Walk_7.png"
        ),
        image.load(
            ".assets/enemies/Bringer-Of-Death/Individual Sprite/Walk/Bringer-of-Death_Walk_8.png"
        ),
    ]
    Flyweight.data["boss_demon_idle"] = [
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/01_demon_idle/demon_idle_1.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/01_demon_idle/demon_idle_2.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/01_demon_idle/demon_idle_3.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/01_demon_idle/demon_idle_4.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/01_demon_idle/demon_idle_5.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/01_demon_idle/demon_idle_6.png"
        ),
    ]
    Flyweight.data["boss_demon_walk"] = [
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/02_demon_walk/demon_walk_1.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/02_demon_walk/demon_walk_2.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/02_demon_walk/demon_walk_3.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/02_demon_walk/demon_walk_4.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/02_demon_walk/demon_walk_5.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/02_demon_walk/demon_walk_6.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/02_demon_walk/demon_walk_7.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/02_demon_walk/demon_walk_8.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/02_demon_walk/demon_walk_9.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/02_demon_walk/demon_walk_10.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/02_demon_walk/demon_walk_11.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/02_demon_walk/demon_walk_12.png"
        ),
    ]
    Flyweight.data["boss_demon_cleave"] = [
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/03_demon_cleave/demon_cleave_1.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/03_demon_cleave/demon_cleave_2.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/03_demon_cleave/demon_cleave_3.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/03_demon_cleave/demon_cleave_4.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/03_demon_cleave/demon_cleave_5.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/03_demon_cleave/demon_cleave_6.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/03_demon_cleave/demon_cleave_7.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/03_demon_cleave/demon_cleave_8.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/03_demon_cleave/demon_cleave_9.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/03_demon_cleave/demon_cleave_10.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/03_demon_cleave/demon_cleave_11.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/03_demon_cleave/demon_cleave_12.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/03_demon_cleave/demon_cleave_13.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/03_demon_cleave/demon_cleave_14.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/03_demon_cleave/demon_cleave_15.png"
        ),
    ]
    Flyweight.data["boss_demon_hit"] = [
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/04_demon_take_hit/demon_take_hit_1.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/04_demon_take_hit/demon_take_hit_2.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/04_demon_take_hit/demon_take_hit_3.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/04_demon_take_hit/demon_take_hit_4.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/04_demon_take_hit/demon_take_hit_5.png"
        ),
    ]
    Flyweight.data["boss_demon_hit"] = [
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/05_demon_death/demon_death_1.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/05_demon_death/demon_death_2.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/05_demon_death/demon_death_3.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/05_demon_death/demon_death_4.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/05_demon_death/demon_death_5.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/05_demon_death/demon_death_6.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/05_demon_death/demon_death_7.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/05_demon_death/demon_death_8.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/05_demon_death/demon_death_9.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/05_demon_death/demon_death_10.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/05_demon_death/demon_death_11.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/05_demon_death/demon_death_12.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/05_demon_death/demon_death_13.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/05_demon_death/demon_death_14.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/05_demon_death/demon_death_15.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/05_demon_death/demon_death_16.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/05_demon_death/demon_death_17.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/05_demon_death/demon_death_18.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/05_demon_death/demon_death_19.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/05_demon_death/demon_death_20.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/05_demon_death/demon_death_21.png"
        ),
        image.load(
            ".assets/enemies/boss_demon_slime_FREE_v1.0/individual sprites/05_demon_death/demon_death_22.png"
        ),
    ]
    Flyweight.data["boss_frost_attack"] = [
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/1_atk/1_atk_1.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/1_atk/1_atk_2.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/1_atk/1_atk_3.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/1_atk/1_atk_4.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/1_atk/1_atk_5.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/1_atk/1_atk_6.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/1_atk/1_atk_7.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/1_atk/1_atk_8.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/1_atk/1_atk_9.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/1_atk/1_atk_10.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/1_atk/1_atk_11.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/1_atk/1_atk_12.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/1_atk/1_atk_13.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/1_atk/1_atk_14.png"
        ),
    ]
    Flyweight.data["boss_frost_death"] = [
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/death/death_1.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/death/death_2.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/death/death_3.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/death/death_4.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/death/death_5.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/death/death_6.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/death/death_7.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/death/death_8.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/death/death_9.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/death/death_10.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/death/death_11.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/death/death_12.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/death/death_13.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/death/death_14.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/death/death_15.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/death/death_16.png"
        ),
    ]
    Flyweight.data["boss_frost_idle"] = [
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/idle/idle_1.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/idle/idle_2.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/idle/idle_3.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/idle/idle_4.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/idle/idle_5.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/idle/idle_6.png"
        ),
    ]
    Flyweight.data["boss_frost_hit"] = [
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/take_hit/take_hit_1.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/take_hit/take_hit_2.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/take_hit/take_hit_3.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/take_hit/take_hit_4.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/take_hit/take_hit_5.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/take_hit/take_hit_6.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/take_hit/take_hit_7.png"
        ),
    ]
    Flyweight.data["boss_frost_walk"] = [
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/walk/walk_1.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/walk/walk_2.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/walk/walk_3.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/walk/walk_4.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/walk/walk_5.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/walk/walk_6.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/walk/walk_7.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/walk/walk_8.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/walk/walk_9.png"
        ),
        image.load(
            ".assets/enemies/Frost_Guardian_FREE_v1.0/PNG files/walk/walk_10.png"
        ),
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
