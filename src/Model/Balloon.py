import Config
import ImageFactory
from Model.Item import Item

class Balloon(Item):

    def __init__(self, speech, position, target):
        self._image = ImageFactory.create_balloon_image_from(speech)
        self._position = position
        self._target = target
        self.speech = speech

    def get_tail_start_at(self, position):
        return (position[0] + self.size[0] / 2, position[1] + self.size[1] - Config.border_width / 2)

    def get_tail_end(self):
        return self._target
