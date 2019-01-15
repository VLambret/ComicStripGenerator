import Config
from Model.PanelItem import PanelItem
from Model.Position import Position
from Model.Position import Type

def parse_position(position_text):
    if position_text[-1] == "%":
        x_type = Type.POURCENTAGE
        x_value_text = position_text[0:-1]
    else:
        x_type = Type.PIXELS
        x_value_text = position_text
    x_value = int(x_value_text)
    return Position((x_value, x_type), (0, Type.POURCENTAGE))

class CharacterLine:

    def __init__(self, line):
        elements = self.character_file = line.strip().split(" ")
        self.character_file = elements[0]
        if(len(elements) > 1):
            self.position = parse_position(elements[1])
        else:
            self.position = Position((50, Type.POURCENTAGE), (0, Type.POURCENTAGE))

    def modify(self, strip):
        character = PanelItem(Config.image_database+"/"+ self.character_file, self.position)
        strip.last_panel().add_panel_item(character)
