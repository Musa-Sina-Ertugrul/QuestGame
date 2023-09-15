"""
    Test file for main.py
"""
import os
import pytest


def test_main():
    """
    Test for game loop
    """
    with pytest.raises(SystemExit):
        os.system("python main.py")
