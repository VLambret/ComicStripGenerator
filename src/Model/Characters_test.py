from Model.Characters import Characters
from Model.Character import Character
from Model.Dialog import Dialog
from Model.PlacedDialog import PlacedDialog

import pytest
import TestFactory

def test_by_default_a_character_list_contains_no_items():
    characters = Characters()
    assert len(characters.get_items()) == 0

def test_given_a_character_is_added_then_items_list_is_one():
    characters = Characters()
    character = TestFactory.character()
    characters.add(character)
    assert len(characters.get_items()) == 1

def test_given_no_dialogs_then_placed_dialogs_is_empty():
    characters = Characters()
    placed_dialogs = characters.place_dialogs([])
    assert placed_dialogs == [[]]

def test_given_a_dialog_from_a_lonely_character_then_dialogs_contains_his_speech():
    characters = Characters()
    character = TestFactory.character_named("Scott")
    characters.add(character)
    dialogs = [Dialog("Scott", "Hello !")]
    placed_dialogs = characters.place_dialogs(dialogs)
    expected_dialogs = [[PlacedDialog("Scott", "Hello !")]]
    assert placed_dialogs == expected_dialogs

NOBODY = []
SINGLE_GUY = [TestFactory.character_named_at("One", TestFactory.LEFT)]
FIRST_LEFT_SECOND_RIGHT = [TestFactory.character_named_at("First", TestFactory.LEFT),
                           TestFactory.character_named_at("Second", TestFactory.RIGHT)]
FIRST_RIGHT_SECOND_LEFT = [TestFactory.character_named_at("First", TestFactory.RIGHT),
                           TestFactory.character_named_at("Second", TestFactory.LEFT)]

SILENCE = []
MONOLOG = [Dialog("First", "A")]
LONG_MONOLOG = [Dialog("First", "A"), Dialog("First", "B")]
EACH_SPEACK_ONCE = [Dialog("First", "A"), Dialog("Second", "B")]
SIMPLE_EXCHANGE = [Dialog("First", "A"), Dialog("Second", "B"), Dialog("First", "C"), Dialog("Second", "D")]

EXPECTED_SILENCE = [[]]
EXPECTED_MONOLOG = [[PlacedDialog("First", "A")]]
EXPECTED_LONG_MONOLOG = [[PlacedDialog("First", "A"), PlacedDialog("First", "B")]]
EXPECTED_EACH_SPEACK_ONCE_FIRST_LEFT = [[PlacedDialog("First", "A"), PlacedDialog("Second", "B")]]
EXPECTED_EACH_SPEACK_ONCE_FIRST_RIGHT = [[PlacedDialog("First", "A")],
                                         [PlacedDialog("Second", "B")]
                                        ]
EXPECTED_EXCHANGE_OUTPUT_FIRST_LEFT = [[PlacedDialog("First", "A"), PlacedDialog("Second", "B")],
                                       [PlacedDialog("First", "C"), PlacedDialog("Second", "D")]
                                      ]
EXPECTED_EXCHANGE_OUTPUT_FIRST_RIGHT = [[PlacedDialog("First", "A")],
                                        [PlacedDialog("Second", "B"), PlacedDialog("First", "C")],
                                        [PlacedDialog("Second", "D")]
                                      ]

@pytest.mark.parametrize("characters, dialogs, expected_placed_dialogs", [
    (NOBODY, SILENCE, EXPECTED_SILENCE),
    (FIRST_LEFT_SECOND_RIGHT, MONOLOG, EXPECTED_MONOLOG),
    (FIRST_RIGHT_SECOND_LEFT, MONOLOG, EXPECTED_MONOLOG),
    (FIRST_LEFT_SECOND_RIGHT, LONG_MONOLOG, EXPECTED_LONG_MONOLOG),
    (FIRST_RIGHT_SECOND_LEFT, LONG_MONOLOG, EXPECTED_LONG_MONOLOG),
    (FIRST_LEFT_SECOND_RIGHT, EACH_SPEACK_ONCE, EXPECTED_EACH_SPEACK_ONCE_FIRST_LEFT),
    (FIRST_RIGHT_SECOND_LEFT, EACH_SPEACK_ONCE, EXPECTED_EACH_SPEACK_ONCE_FIRST_RIGHT),
    (FIRST_LEFT_SECOND_RIGHT, SIMPLE_EXCHANGE, EXPECTED_EXCHANGE_OUTPUT_FIRST_LEFT),
    (FIRST_RIGHT_SECOND_LEFT, SIMPLE_EXCHANGE, EXPECTED_EXCHANGE_OUTPUT_FIRST_RIGHT),
])
def test_dialogs_use_several_levels_when_speeches_are_mixed(characters, dialogs, expected_placed_dialogs):
    actual_characters = Characters()
    for character in characters:
        actual_characters.add(character)

    placed_dialogs = actual_characters.place_dialogs(dialogs)
    assert placed_dialogs == expected_placed_dialogs
