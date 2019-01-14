import Config
from Model.PanelItem import PanelItem
from Model.Panel import Panel

class BackgroundLine:

    def __init__(self):
        pass

    def modify(self, strip):
        background_item = PanelItem(Config.image_database+"/"+ "background.png", (0, 0))
        strip.panels.append(Panel(background_item))
