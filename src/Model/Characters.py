from Model.PlacedDialog import PlacedDialog

class Characters:

    def __init__(self):
        self._characters = []
        pass

    def add(self, character):
        self._characters.append(character)

    def get_items(self):
        return self._characters

    def place_dialogs(self, dialogs):
        result = []
        for dialog in dialogs:
            result.append(PlacedDialog(dialog.name, dialog.speech))
        return result
