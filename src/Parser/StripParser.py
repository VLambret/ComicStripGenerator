#! /usr/bin/python3

import sys
import re
from Model.Strip import Strip
from Model.Panel import Panel
from Model.PanelItem import PanelItem
from Model.Balloon import Balloon
import Config

def is_background(line):
    type_of_item = line.rstrip().split(':')[0]
    return type_of_item == "background"

def is_item(line):
    type_of_item = line.rstrip().split(':')[0]
    return type_of_item == "item"

def is_balloon(line):
    type_of_item = line.rstrip().split(':')[0]
    return type_of_item == "balloon"

def is_config(line):
    # A valid config is a key:value string
    if re.match("[^:]+:[^:]+", line) is None:
        return False

    config_key = line.rstrip().split(':')[0]
    print("config_key:" + config_key)
    return config_key in ["font_name", "font_size", "image_database", "border_width"]

def is_empty_line(line):
    if re.match("^[ \t]*$", line) is not None:
        return True
    return False

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

def create_panel_from_background(config):
    background_file_name = PanelItem(Config.image_database+"/"+ config[1], (0, 0))
    return Panel(background_file_name)

def create_item(panel, config):
    position = (int(config[2]), int(config[3]))
    item = PanelItem(Config.image_database + "/" + config[1], position)
    panel.add_panel_item(item)

def create_balloon(panel, config):
    position = (int(config[1]), int(config[2]))
    tail_angle = int(config[3])
    tail_length = int(config[4])
    speech = config[5].replace("\\n", "\n")
    balloon = Balloon(position, tail_angle, tail_length, speech)
    panel.add_balloon(balloon)

def init_from_file(file_name):
    strip = Strip()
    panel = None
    line_number = 0

    with open(file_name, 'r') as file_opened:
        for line in file_opened:
            line_number += 1
            parsed_line = line.rstrip().split(':')
            type_of_item = parsed_line[0]

            if is_background(line):
                if panel is not None:
                    strip.panels.append(panel)
                panel = create_panel_from_background(parsed_line)
            elif is_item(line):
                create_item(panel, parsed_line)
            elif is_balloon(line):
                create_balloon(panel, parsed_line)
            elif is_config(line):
                set_config(line)
            elif not is_empty_line(line):
                sys.stderr.write("Parsing error line " + str(line_number)  + ": " + line)
        strip.panels.append(panel)
    return strip
