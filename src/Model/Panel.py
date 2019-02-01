from Model.Balloon import Balloon
from Model.Configuration import Configuration
from Model.Position import Type, Position
from Model.Scene import Scene


class Panel:

    def __init__(self, background_panel_item):
        self.config = Configuration()
        self.background = background_panel_item
        self.scene = Scene()
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
            target = self.scene.get_character(dialog[0]).get_top_in(self)
            balloon = Balloon(dialog[1], position, target)
            balloon.place_auto(rank, total, self.config.balloon_padding_pourcentage)
            balloon_list.append(balloon)
            rank = rank + 1

        return balloon_list

    def get_panel_items(self):
        return self.scene.get_items()

    def add_character(self, character):
        self.scene.add(character)

    def add_dialog(self, charater_name, speech):
        self._dialogs.append((charater_name, speech))
