import io

from Model.Strip import Strip
from Parser.StripYacc import parser


def test_parsing_an_empty_files_gives_an_empty_strip():
    input = io.StringIO("")
    strip = parser.parse(input.read())
    assert isinstance(strip, Strip)
    assert len(strip.panels) == 0

#def test_a_line_starting_with_a_sharp_is_an_ignored_comment():
#    input = io.StringIO("#Some comment")
#    strip = StripParser.parse(input)
#    assert isinstance(strip, Strip)
#    assert len(strip.panels) == 0

#def test_a_key_value_separated_with_a_colon_is_a_config_element():
#    input = io.StringIO("database:../../sources")
#    strip = StripParser.parse(input)
#    assert isinstance(strip, Strip)
#    assert len(strip.panels) == 0
#    assert strip.config.database == "../../sources"

