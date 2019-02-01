from Model.PlacedDialog import PlacedDialog

class Scene:

    def __init__(self):
        self._characters = []
        pass

    def add(self, character):
        self._characters.append(character)

    def get_items(self):
        self.place_auto_characters()
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
            if len(current_line) > 0:
                current_character = self.get_character(dialog.name)
                previous_character = self.get_character(current_line[-1].name)
                if current_character.is_before_in_read_order(previous_character):
                    result.append(current_line)
                    current_line = []
            current_line.append(PlacedDialog(dialog.name, dialog.speech))
        result.append(current_line)
        return result

    def place_auto_characters(self):
        total = self.get_auto_placed_characters_number()
        rank = 0
        for c in self._characters:
            if (c.is_auto_placed):
                c.place_auto(rank, total, 0)
                rank = rank + 1

    def get_auto_placed_characters_number(self):
        count = 0
        for c in self._characters:
            if (c.is_auto_placed):
                count = count + 1
        return count
