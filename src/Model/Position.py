import Config

from enum import Enum
class Type(Enum):
    PIXELS = 1
    POURCENTAGE = 2
    AUTO = 3

def get_pixel_position(position, item_length, container_length):
    value = position[0]
    position_type = position[1]
    if position_type is Type.POURCENTAGE:
        return int(float(value) * (container_length - item_length) / 100)
    return value

class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Position):
            return self.x == other.x and self.y == other.y
        return False

    def get_position_in(self, item_box, container):
        container_box = container.size
        x_value = get_pixel_position(self.x, item_box[0], container_box[0])
        # XXX: We prefer (0,0) to be the bottom-left of the image. For PIL it's the bottom-top
        flipped_y = (100 - self.y[0], Type.POURCENTAGE)
        y_value = get_pixel_position(flipped_y, item_box[1], container_box[1])
        return (x_value, y_value)

    def set_auto_position(self, rank, auto_x_element_number, padding):
        if self.x[1] != Type.AUTO:
            return
        value = 50
        if (auto_x_element_number > 1):
            value = padding + (rank * (100 - 2 * padding) / (auto_x_element_number - 1))
        self.x = (value, Type.POURCENTAGE)

