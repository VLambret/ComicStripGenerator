#! /usr/bin/python3

import sys
import re
from Model.Strip import Strip
from Model.Panel import Panel
from Model.PanelItem import PanelItem
from Model.Balloon import Balloon
import Config

from Parser.IgnoredLine import IgnoredLine
from Parser.SeparatorLine import SeparatorLine
from Parser.BackgroundLine import BackgroundLine
from Parser.CharacterLine import CharacterLine
from Parser.ConfigLine import ConfigLine

SPACE = "[ \t]+"
INDENT = "[ \t]*"
COMMENT = INDENT + "(#.*)?"
DEC = "([-+]?[0-9]+)"
FILENAME = "([^ \t\n]+)"
POSITION = r"\(" + DEC + "," + DEC + r"\)"
SPEECH = "([^\n]+)"

IGNORE_REGEX = [COMMENT]
BACKGROUND_REGEX = [INDENT, "=", INDENT, FILENAME, INDENT]
ITEM_REGEX = [INDENT, "@", SPACE, FILENAME, SPACE, POSITION, INDENT]
BALLOON_REGEX = [INDENT, "-", INDENT, POSITION, SPACE, DEC, SPACE, DEC, SPACE, SPEECH]

def parse_lines(lines):
    result = []
    for line in lines:
        parsed_line = identify_line(line)
        result.append(parsed_line)

    return result

def create_strip_from_parsed_lines(parsed_lines):
    strip = Strip()
    for parsed_line in parsed_lines:
        parsed_line.modify(strip)
    return strip

def identify_line(line):
    if (line == "" or line.isspace()):
        return SeparatorLine()
    if (line[0] == "@"):
        return BackgroundLine()
    if (line[0] == "#"):
        return IgnoredLine()
    if(is_config_format(line)):
        return ConfigLine(line)
    return CharacterLine()

def line_regex(description):
    return "^" + "".join(description) + "$"

def is_config_format(line):
    # A valid config is a key:value string
    if re.match("[^:]+:[^:]+", line) is None:
        return False
    return True

def is_config(line):
    if (is_config_format(line)):
        config_key = line.rstrip().split(':')[0]
        return config_key in ["font_name", "font_size", "image_database", "border_width"]
    return False

def is_empty_line(line):
    return re.match(line_regex(IGNORE_REGEX), line) is not None

def set_config(line):
    config_key = line.rstrip().split(':')[0]
    value = line.rstrip().split(':')[1]
    if config_key == "font_name":
        Config.font_name = value
    elif config_key == "font_size":
        Config.font_size = int(value)
    elif config_key == "image_database":
        Config.image_database = value
    elif config_key == "border_width":
        Config.border_width = int(value)

def parse_background(line):
    match = re.match(line_regex(BACKGROUND_REGEX), line)
    if match is None:
        return None
    background_name = match.group(1)
    return PanelItem(Config.image_database+"/"+ background_name, (0, 0))

def parse_item(line):
    match = re.match(line_regex(ITEM_REGEX), line)
    if not match:
        return None
    filename = match.group(1)
    position = (int(match.group(2)), int(match.group(3)))
    return PanelItem(Config.image_database + "/" + filename, position)

def parse_balloon(line):
    match = re.match(line_regex(BALLOON_REGEX), line)
    if not match:
        return None
    position = (int(match.group(1)), int(match.group(2)))
    tail_angle = int(match.group(3))
    tail_length = int(match.group(4))
    speech = match.group(5).strip().replace('\\n', '\n')
    return Balloon(position, tail_angle, tail_length, speech)

def parse_strip(file_content):
    strip = Strip()
    panel = None

    for line in file_content:
        if is_empty_line(line):
            continue

        panel_item = parse_item(line)
        if panel_item is not None:
            panel.add_panel_item(panel_item)
            continue

        background_item = parse_background(line)
        if background_item is not None:
            if panel is not None:
                strip.panels.append(panel)
            panel = Panel(background_item)
            continue

        balloon = parse_balloon(line)
        if balloon is not None:
            panel.add_balloon(balloon)
            continue

        if is_config(line):
            set_config(line)
    if panel is not None:
        strip.panels.append(panel)
    return strip

def init_from_file(file_name):

    with open(file_name, 'r') as file_opened:
        return parse_strip(file_opened)
