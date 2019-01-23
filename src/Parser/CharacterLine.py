import re

import Config
from Model.Character import Character
from Model.Position import Position
from Model.Position import Type

def captured(pattern):
    return pattern

def optional(pattern):
    return "(" + pattern + ")?"

def line_regex(patterns):
    return "^" + "".join(patterns) + "$"

SPACE = "[ \t]+"

POSITION_VALUE = captured("([0-9]+%?)")

POSITION_REGEX = POSITION_VALUE + optional("," + POSITION_VALUE)

DIALOG_REGEX = '"(.+)"'

def parse_position_value(position_value_text):
    if position_value_text[-1] == "%":
        return int(position_value_text[0:-1]), Type.POURCENTAGE
    return int(position_value_text), Type.PIXELS

def parse_position(position_text):
    match = re.match(POSITION_REGEX, position_text)
    if not match:
        return None
    x_text = match.group(1)
    y_text = match.group(2)

    x_value = parse_position_value(x_text)
    if y_text is not None:
        y_value = parse_position_value(y_text[1:])
    else:
        y_value = (0, Type.POURCENTAGE)

    return Position(x_value, y_value)

class CharacterLine:

    def __init__(self, line):
        line = line.strip()
        detect_dialogs = line.split('"', 2)
        if len(detect_dialogs) > 1:
            self.dialog = detect_dialogs[1]
        else:
            self.dialog = None
        line = detect_dialogs[0]

        elements = self.character_file = line.strip().split(" ")
        self.character_file = elements[0]
        if len(elements) > 1:
            self.position = parse_position(elements[1])
        else:
            self.position = Position((0, Type.AUTO), (0, Type.POURCENTAGE))

    def modify(self, strip):
        character = Character("", Config.image_database+"/"+ self.character_file, self.position)
        strip.last_panel().add_character(character)
        if self.dialog:
            strip.last_panel().add_dialog("", self.dialog)
