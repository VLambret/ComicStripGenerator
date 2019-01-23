import pytest

from Parser.CharacterLine import CharacterLine
from Model.Position import Position
from Model.Position import Type

DEFAULT_IMAGE = "narrateur-angry.png"
DEFAULT_CENTER_POSITION = Position((0, Type.AUTO), (0, Type.POURCENTAGE))

@pytest.mark.parametrize("line, expected_image, expected_position", [
    ("narrateur-angry.png", "narrateur-angry.png", DEFAULT_CENTER_POSITION),
    ("narrateur-angry.png 0%", "narrateur-angry.png", Position((0, Type.POURCENTAGE), (0, Type.POURCENTAGE))),
    ("narrateur-angry.png 100%", "narrateur-angry.png", Position((100, Type.POURCENTAGE), (0, Type.POURCENTAGE))),
    ("narrateur-angry.png 0", "narrateur-angry.png", Position((0, Type.PIXELS), (0, Type.POURCENTAGE))),
    ("narrateur-angry.png 246", "narrateur-angry.png", Position((246, Type.PIXELS), (0, Type.POURCENTAGE))),
    ("narrateur-angry.png 0,0", "narrateur-angry.png", Position((0, Type.PIXELS), (0, Type.PIXELS))),
    ("narrateur-angry.png 0,10", "narrateur-angry.png", Position((0, Type.PIXELS), (10, Type.PIXELS))),
    ("narrateur-angry.png 0,10%", "narrateur-angry.png", Position((0, Type.PIXELS), (10, Type.POURCENTAGE))),
])
def test_character_line_parsing(line, expected_image, expected_position):
    character = CharacterLine(line)
    assert character.character_file == expected_image
    assert character.position == expected_position
    assert character.dialog is None

@pytest.mark.parametrize("position_text, dialog_text, expected_position, expected_dialog", [
    ('', '', DEFAULT_CENTER_POSITION, None),
    ('12,34%', '""', Position((12, Type.PIXELS), (34, Type.POURCENTAGE)), ""),
    ('12,34%', '"Hello !"', Position((12, Type.PIXELS), (34, Type.POURCENTAGE)), "Hello !"),
    ('12,34%', '"Bonjour !"', Position((12, Type.PIXELS), (34, Type.POURCENTAGE)), "Bonjour !"),
])
def test_character_line_dialog_parsing(position_text, dialog_text, expected_position, expected_dialog):
    line = " ".join([DEFAULT_IMAGE, position_text, dialog_text])
    character = CharacterLine(line)
    assert character.character_file == DEFAULT_IMAGE
    assert character.position == expected_position
    assert character.dialog == expected_dialog
