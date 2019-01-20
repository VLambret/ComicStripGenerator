import math

import Config
import ImageFactory

class Balloon:

    def __init__(self, speech, position):
        self.image = ImageFactory.create_balloon_image_from(speech)
        self._position = position
        self.speech = speech

    @property
    def size(self):
        return self.image.size

    def get_absolute_position_in(self, box):
        return self._position.get_position_in(self.size, box)

    def get_tail_start_at(self, position):
        return (position[0] + self.size[0] / 2, position[1] + self.size[1] - Config.border_width / 2)

    def get_tail_end_at(self, position):
        tail_angle = 90
        tail_length = 20
        start = self.get_tail_start_at(position)
        offsetx = tail_length * math.cos(math.radians(tail_angle))
        offsety = tail_length * math.sin(math.radians(tail_angle))
        return (start[0] + offsetx, start[1] + offsety)
