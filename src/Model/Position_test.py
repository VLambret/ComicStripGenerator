import pytest

from Model.Position import get_pixel_position
from Model.Position import Type, Position

@pytest.mark.parametrize("position, item_length, container_length, expected_value", [
    ((0, Type.POURCENTAGE), 10, 400, 0),
    ((25, Type.POURCENTAGE), 10, 400, 97),
    ((50, Type.POURCENTAGE), 10, 400, 195),
    ((75, Type.POURCENTAGE), 10, 400, 292),
    ((100, Type.POURCENTAGE), 10, 400, 390),
])
def test_pourcentage_position_value(position, item_length, container_length, expected_value):
    obtained_value = get_pixel_position(position, item_length, container_length)
    assert obtained_value == expected_value

@pytest.mark.parametrize("position, item_length, container_length, expected_value", [
    ((0, Type.PIXELS), 10, 400, 0),
    ((25, Type.PIXELS), 10, 400, 25),
    ((50, Type.PIXELS), 10, 400, 50),
    ((75, Type.PIXELS), 10, 400, 75),
    ((100, Type.PIXELS), 10, 400, 100),
    ((392, Type.PIXELS), 10, 400, 392),
])
def test_pixels_position_value(position, item_length, container_length, expected_value):
    obtained_value = get_pixel_position(position, item_length, container_length)
    assert obtained_value == expected_value

DEFAULT_X = (0, Type.POURCENTAGE)
DEFAULT_Y = (0, Type.POURCENTAGE)

def test_setting_auto_position_changes_nothing_on_non_auto_positons():
    position = Position(DEFAULT_X, DEFAULT_Y)
    position.set_auto_position(0)
    assert position.x == DEFAULT_X
    assert position.y == DEFAULT_Y
