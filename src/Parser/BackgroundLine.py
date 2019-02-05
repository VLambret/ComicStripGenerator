import Config
from Model.Item import Item
from Model.Panel import Panel

class BackgroundLine:

    def __init__(self, line):
        self._background = line[1:].strip()

    def modify(self, strip):
        background_item = Item(Config.image_database + "/" + self._background, (0, 0))
        strip.panels.append(Panel(background_item))
