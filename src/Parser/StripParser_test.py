import Parser.StripParser

def test_is_background():
    result = Parser.StripParser.is_background("")
    assert result is False, "Empty line"

    result = Parser.StripParser.is_background("This is not a background")
    assert result is False, "Invalid background"

    result = Parser.StripParser.is_background("=background.png")
    assert result is True, "valid background"

    result = Parser.StripParser.is_background("     =    background.png     ")
    assert result is True, "valid indented background"

def test_new_panel_from_background_line():
    panel = Parser.StripParser.new_panel_from_background_line("=background.png")
    background_name = panel.get_background().get_image_name()
    assert background_name == "sources/background.png", "valid background"

    panel = Parser.StripParser.new_panel_from_background_line("  =    background.png    ")
    background_name = panel.get_background().get_image_name()
    assert background_name == "sources/background.png", "valid background width spaces"

def test_is_item():
    result = Parser.StripParser.is_item("")
    assert result is False, "Empty line"

    result = Parser.StripParser.is_item("This is not a item")
    assert result is False, "Invalid item"

    result = Parser.StripParser.is_item("@ item.png (0,0)")
    assert result is True, "valid item"

    result = Parser.StripParser.is_item("     @     item.png     (0,0)   ")
    assert result is True, "valid indented item"

def test_is_config():
    result = Parser.StripParser.is_config("")
    assert result is False, "Empty line"

    result = Parser.StripParser.is_config("font_size:40")
    assert result is True, "Should be valid"

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
