import pytest

from Model.Position import Position
from Model.Position import Type

@pytest.mark.parametrize("position, item_length, container_length, expected_value", [
    ((0, Type.POURCENTAGE), 10, 400, 0),
    ((25, Type.POURCENTAGE), 10, 400, 97),
    ((50, Type.POURCENTAGE), 10, 400, 195),
    ((75, Type.POURCENTAGE), 10, 400, 292),
    ((100, Type.POURCENTAGE), 10, 400, 390),
])
def test_pourcentage_position_value(position, item_length, container_length, expected_value):
    value = Position.value(position, item_length, container_length)
    assert value == expected_value

@pytest.mark.parametrize("position, item_length, container_length, expected_value", [
    ((0, Type.PIXELS), 10, 400, 0),
    ((25, Type.PIXELS), 10, 400, 25),
    ((50, Type.PIXELS), 10, 400, 50),
    ((75, Type.PIXELS), 10, 400, 75),
    ((100, Type.PIXELS), 10, 400, 100),
    ((392, Type.PIXELS), 10, 400, 392),
])
def test_pixels_position_value(position, item_length, container_length, expected_value):
    value = Position.value(position, item_length, container_length)
    assert value == expected_value
