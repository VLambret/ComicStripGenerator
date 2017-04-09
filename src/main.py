import argparse
from PanelItem import PanelItem
from Panel import Panel
import StripGenerator
from Balloon import Balloon
from Strip import Strip

def create_panel_from_background(config):
    background_file_name = PanelItem("sources/"+ config[1], (0, 0))
    return Panel(background_file_name)

def create_item(panel, config):
    position = (int(config[2]), int(config[3]))
    item = PanelItem("sources/"+ config[1], position)
    panel.add_panel_item(item)

def create_balloon(panel, config):
    position = (int(config[1]), int(config[2]))
    speacker_position = (int(config[3]), int(config[4]))
    tail_length = int(config[5])
    speech = config[6].replace("\\n", "\n")
    balloon = Balloon(position, speacker_position, tail_length, speech)
    panel.add_balloon(balloon)

def init_from_file(file_name):
    strip = Strip()
    panel = None

    with open(file_name, 'r') as file_opened:
        for line in file_opened:
            parsed_line = line.rstrip().split(':')
            type_of_item = parsed_line[0]

            if type_of_item == "background":
                if panel is not None:
                    strip.panels.append(panel)
                panel = create_panel_from_background(parsed_line)
            elif type_of_item == "item":
                create_item(panel, parsed_line)
            elif type_of_item == "balloon":
                create_balloon(panel, parsed_line)
        strip.panels.append(panel)
    return strip

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', help="comic file to transform into Makefile",
                        default="strip.comic", type=str, required=False)
    args = parser.parse_args()
    return args.f

def main():
    comic_file_name = get_arguments()
    final_png_name = comic_file_name.replace(".comic", ".png")
    strip = init_from_file(comic_file_name)
    StripGenerator.create_image_from_strip(strip, final_png_name)

main()
