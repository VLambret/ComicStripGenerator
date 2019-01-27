from Model.Balloon import Balloon
from Model.Position import Type, Position
import Config
from Model.Configuration import Configuration


class Panel:

    def __init__(self, background_panel_item):
        self.config = Configuration()
        self.background = background_panel_item
        self.characters = []
        self._dialogs = []

    @property
    def size(self):
        return self.background.size

    @property
    def balloons(self):
        balloon_list = []
        total = len(self._dialogs)
        rank = 0
        for dialog in self._dialogs:
            position = Position((0, Type.AUTO), (100 - self.config.balloon_padding_pourcentage, Type.POURCENTAGE))
            target = self.get_character_named(dialog[0]).get_top_in(self)
            balloon = Balloon(dialog[1], position, target)
            balloon.place_auto(rank, total, self.config.balloon_padding_pourcentage)
            balloon_list.append(balloon)
            rank = rank + 1

        return balloon_list

    def get_character_named(self, name):
        for character in self.characters:
            if character.name == name:
                return character
        return None

    def get_panel_items(self):
        self.place_auto_characters()
        return self.characters

    def add_character(self, character):
        self.characters.append(character)

    def add_dialog(self, charater_name, speech):
        self._dialogs.append((charater_name, speech))

    def place_auto_characters(self):
        total = self.get_auto_placed_characters_number()
        rank = 0
        for c in self.characters:
            if (c.is_auto_placed):
                c.place_auto(rank, total, 0)
                rank = rank + 1

    def get_auto_placed_characters_number(self):
        count = 0
        for c in self.characters:
            if (c.is_auto_placed):
                count = count + 1
        return count
