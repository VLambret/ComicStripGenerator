from PIL import Image

import Config
from Model.Item import Item
from Model.Panel import Panel

class BackgroundLine:

    def __init__(self, line):
        self._background = line[1:].strip()

    def modify(self, strip):
        image_path = Config.image_database + "/" + self._background
        image = Image.open(image_path)
        background_item = Item(image, (0, 0))
        strip.panels.append(Panel(background_item))
