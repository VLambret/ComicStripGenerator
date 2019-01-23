import pytest

from Model.Panel import Panel
from Model.Position import Type
from Model.Position import Position
from Model.Character import Character
import Config

DEFAULT_BACKGROUND = "background.png"
DEFAULT_IMAGE = Config.image_database+"/narrateur-smiling.png"

def test_panel_instance():
    panel = Panel(DEFAULT_BACKGROUND)

def test_a_created_panel_contains_no_auto_placed_characters():
    panel = Panel(DEFAULT_BACKGROUND)
    assert panel.get_auto_placed_characters_number() == 0

def test_when_a_auto_placed_character_is_added_to_panel_the_total_is_updated():
    panel = Panel(DEFAULT_BACKGROUND)
    for counter in range(1, 10):
        name = "john doe " + str(counter)
        auto_position = Position((counter, Type.AUTO), (0, Type.POURCENTAGE))
        new_character = Character(name, DEFAULT_IMAGE, auto_position)
        panel.add_character(new_character)
        assert panel.get_auto_placed_characters_number() == counter
