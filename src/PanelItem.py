from PIL import Image

class PanelItem:

    def __init__(self, image_name, position):
        self.image_name = image_name
        self.size = Image.open(self.image_name).size
        self.position = position

    def get_size(self):
        return self.size

    def get_image_name(self):
        return self.image_name
