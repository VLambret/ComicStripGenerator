from Model.Characters import Characters
from Model.Character import Character
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
    assert len(placed_dialogs) == 0
