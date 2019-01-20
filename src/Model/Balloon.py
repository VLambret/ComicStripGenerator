import ImageFactory

class Balloon:

    def __init__(self, speech, position):
        self.image = ImageFactory.create_balloon_image_from(speech)
        self._position = position
        self.tail_angle = 90
        self.tail_length = 20
        self.speech = speech

    @property
    def size(self):
        return self.image.size

    def get_absolute_position_in(self, box):
        return self._position.get_position_in(self.size, box)
