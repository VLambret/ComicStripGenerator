import Config
from Model.PanelItem import PanelItem
from Model.Position import Position
from Model.Position import Type

class CharacterLine:

    def __init__(self, line):
        self.character_file = line.strip()
        self.position = Position((50, Type.POURCENTAGE), (0, Type.POURCENTAGE))

    def modify(self, strip):
        character = PanelItem(Config.image_database+"/"+ self.character_file, self.position)
        strip.last_panel().add_panel_item(character)
