import pytest

import TestFactory

LEFT = TestFactory.LEFT
MIDDLE = TestFactory.MIDDLE
RIGHT = TestFactory.RIGHT

@pytest.mark.parametrize("first_position, second_position, expected_result", [
    #(LEFT, LEFT, True),
    (LEFT, MIDDLE, True),
    (LEFT, RIGHT, True),
    (MIDDLE, LEFT, False),
    #(MIDDLE, MIDDLE, True),
    (MIDDLE, RIGHT, True),
    (RIGHT, LEFT, False),
    (RIGHT, MIDDLE, False),
    #(RIGHT, RIGHT, True),
])
def test_verify_read_order_for_characters(first_position, second_position, expected_result):
    first = TestFactory.character_at(first_position)
    second = TestFactory.character_at(second_position)
    result = first.is_before_in_read_order(second)
    assert result == expected_result
