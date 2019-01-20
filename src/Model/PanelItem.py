from PIL import Image

class PanelItem:

    def __init__(self, image_name, position):
        self.image = Image.open(image_name)
        self._position = position

    @property
    def size(self):
        return self.image.size

    def get_absolute_position_in(self, box):
        return self._position.get_position_in(self.size, box)
