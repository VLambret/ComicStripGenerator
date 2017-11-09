import re
from PIL import Image

NATURAL_POSITIONS = {
    'left' :  (0, 0),
    'middle' :  (50, 0),
    'right' :  (100, 0),
    'center-left' :  (0, 50),
    'center' :  (50, 50),
    'center-right' :  (100, 50),
    'top-left' :  (0, 100),
    'top' :  (50, 100),
    'top-right' :  (100, 100),
    }

def get_pixels(line):
    match = re.match("([0-9]+),([0-9]+)", line.replace(" ", ""))
    if not match:
        return None
    return (int(match.group(1)), int(match.group(2)))

def get_percentage(line):
    match = re.match("([0-9]+)%,([0-9]+)%", line.replace(" ", ""))
    if not match:
        return None
    return (int(match.group(1)), int(match.group(2)))

def get_position_from_percentage(percentage, box_length, item_length):
    if box_length <= item_length:
        return 0
    return ((box_length - item_length) * percentage) / 100

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


    def get_position_in_box(self, box):
        try:
            percentage_pos = NATURAL_POSITIONS[self._position]
            return (get_position_from_percentage(percentage_pos[0], box[0], self._size[0]),
                    get_position_from_percentage(percentage_pos[1], box[1], self._size[1]))
        except:
            pass

        percentage_pos = get_percentage(self._position)
        if percentage_pos is not None:
            return (get_position_from_percentage(percentage_pos[0], box[0], self._size[0]),
                    get_position_from_percentage(percentage_pos[1], box[1], self._size[1]))

        return get_pixels(self._position)
