from Model.Balloon import Balloon
from Model.Position import Type, Position


class Panel:

    def __init__(self, background_panel_item):
        self.background = background_panel_item
        self.characters = []
        self._dialogs = []

    @property
    def size(self):
        return self.background.get_size()

    @property
    def balloons(self):
        balloon_list = []
        for dialog in self._dialogs:
            balloon_list.append(Balloon(dialog[1], Position((0, Type.POURCENTAGE), (100, Type.POURCENTAGE))))
        return balloon_list

    def get_panel_items(self):
        return self.characters

    def add_character(self, character):
        self.characters.append(character)

    def add_dialog(self, charater_name, speech):
        self._dialogs.append((charater_name, speech))
