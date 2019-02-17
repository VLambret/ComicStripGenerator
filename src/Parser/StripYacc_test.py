import io

import pytest

import Config
from Model.Strip import Strip
from Parser.StripYacc import parser

class Source():

    def __init__(self):
        self.lines = []
        self.database = ""

    def addPanel(self):
        if not self.database:
            #self.with_database("../../sources")
            self.with_database("sources")
        self.lines.append("@background.png")
        return self

    def with_database(self, database):
        self.database = 'database:' + database
        return self

    def build(self):
        content = "\n".join([self.database] + self.lines)
        print(content)
        return io.StringIO(content)

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
    input = Source().with_database(value).build()
    strip = parser.parse(input.read())
    assert isinstance(strip, Strip)
    assert len(strip.panels) == 0
    assert Config.image_database == value

@pytest.mark.parametrize("expected_panel_number", [1, 2, 3])
def test_a_line_starting_with_an_arobase_is_a_new_panel(expected_panel_number):
    source = Source()
    panel_number = 0
    while panel_number < expected_panel_number:
        source.addPanel()
        panel_number +=1

    input = source.build()
    strip = parser.parse(input.read())
    assert isinstance(strip, Strip)
    assert len(strip.panels) == expected_panel_number

