from Model.Coordinates import Coordinates
from Model.Position import Type


class Item:

    def __init__(self, image, position):
        self._image = image
        self._position = position

    @property
    def image(self):
        return self._image

    @property
    def size(self):
        return self.image.size

    @property
    def is_auto_placed(self):
        return self._position.x[1] == Type.AUTO

    def get_coordinates_in(self, container):
        absolute_position = self._position.get_position_in(self.size, container)
        return Coordinates(absolute_position[0], absolute_position[1]).toTuple()

    def place_auto(self, rank, total, padding):
        self._position.set_auto_position(rank, total, padding)
