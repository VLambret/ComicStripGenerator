#! /usr/bin/python3

import re

import Config
from Model.Balloon import Balloon
from Model.PanelItem import PanelItem
from Model.Strip import Strip
from Parser.BackgroundLine import BackgroundLine
from Parser.CharacterLine import CharacterLine
from Parser.ConfigLine import ConfigLine
from Parser.IgnoredLine import IgnoredLine
from Parser.SeparatorLine import SeparatorLine

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
    if line == "" or line.isspace():
        return SeparatorLine()
    if line[0] == "@":
        return BackgroundLine()
    if line[0] == "#":
        return IgnoredLine()
    if is_config_format(line):
        return ConfigLine(line)
    return CharacterLine(line)

def line_regex(description):
    return "^" + "".join(description) + "$"

def is_config_format(line):
    # A valid config is a key:value string
    if re.match("[^:]+:[^:]+", line) is None:
        return False
    return True

def is_config(line):
    if is_config_format(line):
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
    return Balloon(speech, position)

def parse_strip(file_content):
    parsed_lines = parse_lines(file_content)
    return create_strip_from_parsed_lines(parsed_lines)

def init_from_file(file_name):

    with open(file_name, 'r') as file_opened:
        return parse_strip(file_opened)
