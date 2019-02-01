from Model.Dialog import Dialog

class PlacedDialog(Dialog):

    def __eq__(self, other):
        if isinstance(other, PlacedDialog):
            return self.name == other.name and self.speech == other.speech
        return False
