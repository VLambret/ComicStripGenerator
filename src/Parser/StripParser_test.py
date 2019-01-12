import Parser.StripParser

from Parser.IgnoredLine import IgnoredLine
from Parser.SeparatorLine import SeparatorLine

def test_a_line_starting_with_a_sharp_caracter_is_a_comment():
    result = Parser.StripParser.identify("# I'am a comment !")
    assert type(result) is IgnoredLine

def test_an_empty_line_is_a_separator():
    result = Parser.StripParser.identify("")
    assert type(result) is SeparatorLine
