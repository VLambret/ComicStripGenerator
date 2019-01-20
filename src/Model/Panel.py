class Panel:

    def __init__(self, background_panel_item):
        self.background = background_panel_item
        self.panel_items = [background_panel_item]
        self.characters = []
        self.balloons = []

    @property
    def size(self):
        return self.background.get_size()

    def add_panel_item(self, panel_item):
        self.panel_items.append(panel_item)

    def add_balloon(self, balloon):
        self.balloons.append(balloon)

    def get_panel_items(self):
        return self.characters + self.panel_items[1:]

    def add_character(self, character):
        self.characters.append(character)
