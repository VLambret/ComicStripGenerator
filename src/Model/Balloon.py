import Config
import ImageFactory
from Model.Item import Item

class Balloon(Item):

    def __init__(self, speech, position, target):
        image = ImageFactory.create_balloon_image_from(speech)
        super().__init__(image, position)
        self._target = target

    def get_tail_start_at(self, position):
        return (position[0] + self.size[0] / 2, position[1] + self.size[1] - Config.border_width / 2)

    def get_tail_end(self):
        return self._target
