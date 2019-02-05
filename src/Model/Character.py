from Model.Item import Item

class Character(Item):

    def __init__(self, name, image_name, position):
        super().__init__(image_name, position)
        self.name = name
        self.name_id = name

    def get_top_in(self, container):
        position = self.get_coordinates_in(container)
        # XXX : Another PIL coordinate conversion that should be put elsewhere
        return position[0] + self.size[0] / 2, container.size[1] - self.size[1]

    def is_before_in_read_order(self, other_character):
        return self._position.x[0] < other_character._position.x[0]

    def __repr__(self):
        position = self._position
        x_text = position.repr_axe(position.x[0], position.x[1])
        y_text = position.repr_axe(position.y[0], position.y[1])
        return "'{0}' : at({1}, {2})".format(self.name, x_text, y_text)
