import pytest

import Config
from Parser.BackgroundLine import BackgroundLine
from Model.Strip import Strip

DEFAULT_BACKGROUND = "background.png"

def test_instance():
    background_line = BackgroundLine("@background.png")

@pytest.mark.parametrize("background_image, expected_size", [
    ("background-white-800x400.png" , (800, 400)),
    ("background-white-1600x800.png", (1600, 800)),
])
def test_the_word_after_the_arobase_is_the_background_image(background_image, expected_size):
    line = "@" + background_image
    background_line = BackgroundLine(line)
    strip = Strip()
    background_line.modify(strip)

    assert len(strip.panels) == 1
    assert strip.panels[0].background.size == expected_size
