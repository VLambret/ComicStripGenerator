from Model.PanelItem import PanelItem

class Character(PanelItem):

    def __init__(self, name, image_name, position):
        super().__init__(image_name, position)
        self.name = name

    def get_top_in(self, box):
        position = self.get_absolute_position_in(box)
        # XXX : Another PIL coordinate conversion that should be put elsewhere
        return position[0] + self.size[0] / 2, box[1] - self.size[1]
