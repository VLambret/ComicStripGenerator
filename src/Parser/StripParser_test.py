import Parser.StripParser

def test_parse_background():
    result = Parser.StripParser.parse_background("")
    assert result is None, "Empty line"

    result = Parser.StripParser.parse_background("This is not a background")
    assert result is None, "Invalid background"

    result = Parser.StripParser.parse_background("=background.png")
    assert result is not None, "valid background"
    background_name = result.get_image_name()
    assert background_name == "sources/background.png", "valid background"

    result = Parser.StripParser.parse_background("     =    background.png     ")
    assert result is not None, "valid indented background"
    background_name = result.get_image_name()
    assert background_name == "sources/background.png", "valid background with spaces"

def test_parse_item():
    result = Parser.StripParser.parse_item("")
    assert result is None, "Empty line"

    result = Parser.StripParser.parse_item("This is not a item")
    assert result is None, "Invalid item"

    result = Parser.StripParser.parse_item("@ perso1.png (0,0)")
    assert result is not None, "valid item detection"
    assert result.get_image_name() == "sources/perso1.png", "valid item image name"
    assert result.get_position() == (0, 0), "valid item position"

    result = Parser.StripParser.parse_item("     @     perso1.png     (0,0)   ")
    assert result is not None, "valid item with spaces detection"
    assert result.get_image_name() == "sources/perso1.png", "valid item with spaces image name"
    assert result.get_position() == (0, 0), "valid item with spaces position"

def test_is_config():
    result = Parser.StripParser.is_config("")
    assert result is False, "Empty line"

    result = Parser.StripParser.is_config("font_size:40")
    assert result is True, "Should be valid"

    result = Parser.StripParser.is_config("unknown_key:strange_value")
    assert result is False, "We should not accept unknown keys"

def test_is_empty_line():
    result = Parser.StripParser.is_empty_line("")
    assert result is True, "Empty line"
    result = Parser.StripParser.is_empty_line("      ")
    assert result is True, "Empty line with spaces"
    result = Parser.StripParser.is_empty_line("	        ")
    assert result is True, "Empty line with mixed tab and spaces"
    result = Parser.StripParser.is_empty_line("	a        ")
    assert result is False, "Not empty line"

    result = Parser.StripParser.is_empty_line("# Comment")
    assert result is True, "Comment"
    result = Parser.StripParser.is_empty_line("     # Indented comment")
    assert result is True, "Indented comment"
