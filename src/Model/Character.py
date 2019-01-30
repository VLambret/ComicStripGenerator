from Model.PanelItem import PanelItem

class Character(PanelItem):

    def __init__(self, name, image_name, position):
        super().__init__(image_name, position)
        self.name = name

    def get_top_in(self, container):
        position = self.get_absolute_position_in(container)
        # XXX : Another PIL coordinate conversion that should be put elsewhere
        return position[0] + self.size[0] / 2, container.size[1] - self.size[1]

    def is_before_in_read_order(self, other_character):
        return self._position.x[0] < other_character._position.x[0]
