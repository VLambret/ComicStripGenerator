import pytest

from Parser.CharacterLine import CharacterLine
from Model.Position import Position
from Model.Position import Type

@pytest.mark.parametrize("line, expected_image, expected_position", [
    ("narrateur-angry.png", "narrateur-angry.png", Position((50, Type.POURCENTAGE), (0, Type.POURCENTAGE))),
])
def test_character_line_parsing(line, expected_image, expected_position):
    c = CharacterLine(line)
    assert c.character_file == expected_image
    assert c.position == expected_position
