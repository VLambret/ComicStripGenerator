from Model.Balloon import Balloon
from Model.Position import Type, Position


class Panel:

    def __init__(self, background_panel_item):
        self.background = background_panel_item
        self.characters = []
        self._dialogs = []

    @property
    def size(self):
        return self.background.size

    @property
    def balloons(self):
        balloon_list = []
        for dialog in self._dialogs:
            position = Position((50, Type.POURCENTAGE), (100, Type.POURCENTAGE))
            target = self.get_character_named(dialog[0]).get_top_in(self)
            balloon_list.append(Balloon(dialog[1], position, target))
        return balloon_list

    def get_character_named(self, name):
        for character in self.characters:
            if character.name == name:
                return character
        return None

    def get_panel_items(self):
        return self.characters

    def add_character(self, character):
        self.characters.append(character)

    def add_dialog(self, charater_name, speech):
        self._dialogs.append((charater_name, speech))

    def get_auto_placed_characters_number(self):
        count = 0
        for c in self.characters:
            if (c.is_auto_placed):
                count = count + 1
        return count
