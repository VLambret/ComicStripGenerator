from PIL import Image

class PanelItem:

    def __init__(self, image_name, position):
        self.image = Image.open(image_name)
        self._position = position

    @property
    def size(self):
        return self.image.size

    def get_position(self):
        return self._position

    def set_position(self, position):
        self._position = position

