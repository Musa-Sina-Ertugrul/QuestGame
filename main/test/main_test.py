"""
    Test file for main.py
"""
import os
import pytest
from main import main


def test_main():
    """
    Test for game loop
    """
    with pytest.raises(SystemExit):
        os.system("python main/main.py")
        main()
