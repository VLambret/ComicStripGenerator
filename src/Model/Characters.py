from Model.PlacedDialog import PlacedDialog

class Characters:

    def __init__(self):
        self._characters = []
        pass

    def add(self, character):
        self._characters.append(character)

    def get_items(self):
        return self._characters

    def get_character(self, name):
        for character in self._characters:
            if (character.name == name):
                return character
        return None

    def place_dialogs(self, dialogs):
        result = []
        current_line = []
        for dialog in dialogs:
            if len(current_line) >= 1:
                current_character = self.get_character(dialog.name)
                previous_character = self.get_character(current_line[-1].name)
                if current_character.is_before_in_read_order(previous_character):
                    result.append(current_line)
                    current_line = []
            current_line.append(PlacedDialog(dialog.name, dialog.speech))
        result.append(current_line)
        return result
