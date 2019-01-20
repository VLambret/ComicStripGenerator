from Model.Balloon import Balloon

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
            balloon_list.append(Balloon((0, 0), 90, 20, dialog[1]))
        return balloon_list

    def get_panel_items(self):
        return self.characters

    def add_character(self, character):
        self.characters.append(character)

    def add_dialog(self, charater_name, speech):
        self._dialogs.append((charater_name, speech))
