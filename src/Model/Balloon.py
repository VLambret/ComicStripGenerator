import Config
import ImageFactory

class Balloon:

    def __init__(self, speech, position, target):
        self.image = ImageFactory.create_balloon_image_from(speech)
        self._position = position
        self._target = target
        self.speech = speech

    @property
    def size(self):
        return self.image.size

    def get_absolute_position_in(self, box):
        return self._position.get_position_in(self.size, box)

    def get_tail_start_at(self, position):
        return (position[0] + self.size[0] / 2, position[1] + self.size[1] - Config.border_width / 2)

    def get_tail_end(self):
        return self._target
