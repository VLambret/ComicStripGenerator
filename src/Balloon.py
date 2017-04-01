class Balloon:

    def __init__(self, speech, offset, orientation, position):
        self._speech = speech
        self._offset = offset
        self._orientation = orientation
        self._position = position

    def get_speech(self):
        return self._speech

    def get_offset(self):
        return self._offset

    def get_horizontal_orientation(self):
        return self._orientation[0]

    def get_vertical_orientation(self):
        return self._orientation[1]

    def get_position(self):
        return self._position
