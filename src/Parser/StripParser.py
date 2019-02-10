#! /usr/bin/python3

import re

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
        return BackgroundLine(line)
    if line[0] == "#":
        return IgnoredLine()
    if is_config_format(line):
        return ConfigLine(line)
    return CharacterLine(line)

def is_config_format(line):
    # A valid config is a key:value string
    if re.match("[^:]+:[^:]+", line) is None:
        return False
    return True

def parse_strip(file_content):
    parsed_lines = parse_lines(file_content)
    return create_strip_from_parsed_lines(parsed_lines)

def init_from_file(file_name):

    with open(file_name, 'r') as file_opened:
        return parse_strip(file_opened)
