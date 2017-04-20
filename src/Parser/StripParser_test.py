import Parser.StripParser

def test_empty_config():
    result = Parser.StripParser.is_config("")
    assert result is False, "Empty line"

def test_valid_config():
    result = Parser.StripParser.is_config("font_size:40")
    assert result is True, "Should be valid"

def test_unknown_config_key():
    result = Parser.StripParser.is_config("unknown_key:strange_value")
    assert result is False, "We should not accept unknown keys"

def test_empty_line():
    result = Parser.StripParser.is_empty_line("")
    assert result is True, "Empty line"
    result = Parser.StripParser.is_empty_line("      ")
    assert result is True, "Empty line with spaces"
    result = Parser.StripParser.is_empty_line("	        ")
    assert result is True, "Empty line with mixed tab and spaces"
    result = Parser.StripParser.is_empty_line("	a        ")
    assert result is False, "Not empty line"
