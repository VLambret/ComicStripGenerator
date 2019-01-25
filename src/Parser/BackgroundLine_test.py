import pytest

from Parser.BackgroundLine import BackgroundLine

DEFAULT_BACKGROUND = "background.png"

def test_instance():
    background = BackgroundLine("@background.png")
