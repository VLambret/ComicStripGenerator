from Model.Character import Character

import pytest
import TestFactory

LEFT_GUY = TestFactory.character_at(TestFactory.LEFT)
MIDDLE_GUY = TestFactory.character_at(TestFactory.MIDDLE)
RIGHT_GUY = TestFactory.character_at(TestFactory.RIGHT)

@pytest.mark.parametrize("first, second, expected_result", [
    #(LEFT_GUY, LEFT_GUY, True),
    (LEFT_GUY, MIDDLE_GUY, True),
    (LEFT_GUY, RIGHT_GUY, True),
    (MIDDLE_GUY, LEFT_GUY, False),
    #(MIDDLE_GUY, MIDDLE_GUY, True),
    (MIDDLE_GUY, RIGHT_GUY, True),
    (RIGHT_GUY, LEFT_GUY, False),
    (RIGHT_GUY, MIDDLE_GUY, False),
    #(RIGHT_GUY, RIGHT_GUY, True),
])
def test_verify_read_order_for_characters(first, second, expected_result):
    result = first.is_before_in_read_order(second)
    assert result == expected_result
