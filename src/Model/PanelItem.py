from PIL import Image

class PanelItem:

    def __init__(self, image_name, position):
        self._image_name = image_name
        self._size = Image.open(self._image_name).size
        self._position = position

    def get_size(self):
        return self._size

    def get_image_name(self):
        return self._image_name

    def get_position(self):
        return self._position
