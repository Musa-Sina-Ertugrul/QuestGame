"""sumary_line

Keyword arguments:
argument -- description
Return: return_description

TODO: Update Docstrings

"""
from typing import Callable, Tuple


def singelton(cls: Callable) -> Tuple[object]:
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
            return singelton.instance
        else:
            singelton.instance: Tuple[object] = (cls(),)
            return singelton.instance

    return inner_singelton(cls)
