from enum import Enum
class Type(Enum):
    PIXELS = 1
    POURCENTAGE = 2
    AUTO = 3

class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def value(position, item_length, container_length):
        value = position[0]
        type = position[1]
        if type is Type.POURCENTAGE:
            return int(float(value) * (container_length - item_length) / 100)
        return 0

    def get_position_in(self, item_box, container_box):
        x_value = Position.value(self.x, item_box[0], container_box[0])
        # We prefer (0,0) to be the bottom-left of the image. For PIL it's
        flipped_y = (100 - self.y[0], Type.POURCENTAGE)
        y_value = Position.value(flipped_y, item_box[1], container_box[1])
        return (x_value, y_value)

