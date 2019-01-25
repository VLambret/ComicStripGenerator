import Config
from Model.PanelItem import PanelItem
from Model.Panel import Panel

class BackgroundLine:

    def __init__(self, line):
        self._background = line[1:].strip()

    def modify(self, strip):
        background_item = PanelItem(Config.image_database+"/" + self._background, (0, 0))
        strip.panels.append(Panel(background_item))
