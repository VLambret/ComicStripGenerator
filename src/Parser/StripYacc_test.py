import io

import pytest

import Config
from Model.Strip import Strip
from Parser.StripYacc import parser


def test_parsing_an_empty_files_gives_an_empty_strip():
    input = io.StringIO("")
    strip = parser.parse(input.read())
    assert isinstance(strip, Strip)
    assert len(strip.panels) == 0

def test_a_line_starting_with_a_sharp_is_an_ignored_comment():
    input = io.StringIO("#Some comment")
    strip = parser.parse(input.read())
    assert isinstance(strip, Strip)
    assert len(strip.panels) == 0

def test_multiline_comment():
    input = io.StringIO("#Some comment\n#Another Comment\n#AndALastOne")
    strip = parser.parse(input.read())
    assert isinstance(strip, Strip)
    assert len(strip.panels) == 0

@pytest.mark.parametrize("key, value", [
    ("database", "toto"),
    ("database", "../../sources"),
])
def test_a_key_value_separated_with_a_colon_is_a_config_element(key, value):
    input = io.StringIO(key + ":" + value)
    strip = parser.parse(input.read())
    assert isinstance(strip, Strip)
    assert len(strip.panels) == 0
    assert Config.image_database == value

