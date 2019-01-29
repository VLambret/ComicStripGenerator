class PlacedDialog:

    def __init__(self, name, speech):
        self.name = name
        self.speech = speech

    def __eq__(self, other):
        if isinstance(other, PlacedDialog):
            return self.name == other.name and self.speech == other.speech
        return False

