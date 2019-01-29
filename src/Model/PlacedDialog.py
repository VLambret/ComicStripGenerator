from Model.Dialog import Dialog

class PlacedDialog(Dialog):

    def __init__(self, name, speech):
        super().__init__(name, speech)

    def __eq__(self, other):
        if isinstance(other, PlacedDialog):
            return True
            return self.name == other.name and self.speech == other.speech
        return False
