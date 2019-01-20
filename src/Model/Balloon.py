import ImageFactory

class Balloon:

    def __init__(self, speech, position):
        self.image = ImageFactory.create_balloon_image_from(speech)
        self.position = position
        self.tail_angle = 90
        self.tail_length = 20
        self.speech = speech
