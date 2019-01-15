import Config
from Model.PanelItem import PanelItem

class CharacterLine:

    def __init__(self, line):
        self.character_file = line.strip()

    def modify(self, strip):
        panel = strip.panels[-1]
        panel_size = panel.get_size()

        character = PanelItem(Config.image_database+"/"+ self.character_file, (0,0))
        character_size = character.get_size()

        position = (int(panel_size[0] / 2 - character_size[0] / 2), int(panel_size[1] - character_size[1]))
        character.set_position(position)
        panel.add_panel_item(character)
