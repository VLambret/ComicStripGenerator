import pytest

import Parser.StripParser

from Parser.IgnoredLine import IgnoredLine
from Parser.SeparatorLine import SeparatorLine
from Parser.BackgroundLine import BackgroundLine
from Parser.CharacterLine import CharacterLine
from Parser.ConfigLine import ConfigLine
import Config

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

@pytest.mark.parametrize("line", ["david", "bernard"])
def test_by_default_a_line_with_at_least_a_name_is_a_character(line):
    result = Parser.StripParser.identify_line(line)
    assert type(result) is CharacterLine

@pytest.mark.parametrize("line", ["database:sources"])
def test_a_config_line_is_a_key_value_separated_by_a_colon(line):
    result = Parser.StripParser.identify_line(line)
    assert type(result) is ConfigLine

def test_parsing_an_empty_file_gives_an_empty_line_list():
    empty_file = [""]
    result = Parser.StripParser.parse_lines(empty_file)
    assert len(result) == 1
    assert type(result[0]) is SeparatorLine

def test_parsing_a_file_with_a_single_background():
    background_file = ["@background.png"]
    parsed_lines = Parser.StripParser.parse_lines(background_file)
    assert len(parsed_lines) == 1
    assert type(parsed_lines[0]) is BackgroundLine

    strip = Parser.StripParser.create_strip_from_parsed_lines(parsed_lines)
    assert len(strip.panels) == 1

def test_parsing_a_file_with_a_config_option():
    background_file = ["database:some_new_path"]
    parsed_lines = Parser.StripParser.parse_lines(background_file)
    assert len(parsed_lines) == 1
    assert type(parsed_lines[0]) is ConfigLine

    strip = Parser.StripParser.create_strip_from_parsed_lines(parsed_lines)
    assert len(strip.panels) == 0
    assert Config.image_database == "some_new_path"
