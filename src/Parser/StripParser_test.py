import pytest

import Parser.StripParser

from Parser.IgnoredLine import IgnoredLine
from Parser.SeparatorLine import SeparatorLine
from Parser.BackgroundLine import BackgroundLine
from Parser.CharacterLine import CharacterLine

def test_a_line_starting_with_a_sharp_caracter_is_a_comment():
    result = Parser.StripParser.identify_line("# I'am a comment !")
    assert type(result) is IgnoredLine

def test_an_empty_line_is_a_separator():
    result = Parser.StripParser.identify_line("")
    assert type(result) is SeparatorLine

@pytest.mark.parametrize("line", ["", "  ", "\t", "\t\t", " \t \t"])
def test_containing_only_spaces_or_tabs_is_a_separator(line):
    result = Parser.StripParser.identify_line(line)
    assert type(result) is SeparatorLine

@pytest.mark.parametrize("line", ["@", "@mountain"])
def test_a_line_starting_with_arobase_is_a_background(line):
    result = Parser.StripParser.identify_line(line)
    assert type(result) is BackgroundLine

@pytest.mark.parametrize("line", ["david", "bernard \"Hello, I'm Bernard !\""])
def test_by_default_a_line_with_at_least_a_name_is_a_character(line):
    result = Parser.StripParser.identify_line(line)
    assert type(result) is CharacterLine
