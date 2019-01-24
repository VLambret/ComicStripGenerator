from PIL import Image
from Model.Position import Type

class PanelItem:

    def __init__(self, image_name, position):
        self.image = Image.open(image_name)
        self._position = position

    @property
    def size(self):
        return self.image.size

    @property
    def is_auto_placed(self):
        return self._position.x[1] == Type.AUTO

    def get_absolute_position_in(self, container):
        return self._position.get_position_in(self.size, container)

    def place_auto(self, rank, total):
        self._position.set_auto_position(rank, total)
