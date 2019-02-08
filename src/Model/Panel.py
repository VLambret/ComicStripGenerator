from Model.Balloon import Balloon
from Model.Configuration import Configuration
from Model.Dialog import Dialog
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
        placed_balloons = self.scene.place_dialogs(self._dialogs)
        balloon_list = []
        rank = 0
        offset = 0
        for balloon_line in placed_balloons:
            total = len(balloon_line)
            for dialog in balloon_line:
                character = self.scene.get_character(dialog.name)
                position = Position((0, Type.AUTO), (100 - self.config.balloon_padding_pourcentage - offset, Type.POURCENTAGE))
                target = character.get_top_in(self)
                balloon = Balloon(dialog.speech, position, target)
                balloon.place_auto(rank, total, self.config.balloon_padding_pourcentage)
                balloon_list.append(balloon)
                rank = rank + 1
            offset = offset + 15

        return balloon_list

    def get_panel_items(self):
        return self.scene.get_items()

    def add_character(self, character):
        self.scene.add(character)

    def add_dialog(self, character_name, speech):
        self._dialogs.append(Dialog(character_name, speech))
