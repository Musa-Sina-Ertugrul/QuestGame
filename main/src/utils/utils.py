"""sumary_line

Keyword arguments:
argument -- description
Return: return_description

TODO: Update Docstrings

"""
from typing import Callable, Dict, Tuple


def singelton(cls: Callable) -> Tuple[Tuple[object]]:
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    def inner_singelton(cls: Callable):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """

        if hasattr(singelton, "instance"):
            if str(cls.__class__) in singelton.instance:
                return ((singelton.instance[str(cls.__class__)],),)
            else:
                singelton.instance[str(cls.__class__)] = cls()
                return ((singelton.instance[str(cls.__class__)],),)
        else:
            singelton.instance: Dict[object] = { str(cls.__class__) : cls()}
            return ((singelton.instance[str(cls.__class__)],),)

    return inner_singelton(cls)
