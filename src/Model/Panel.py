class Panel:

    def __init__(self, background_panel_item):
        self.size = background_panel_item.get_size()
        self.panel_items = [background_panel_item]
        self.characters = []
        self.balloons = []

    def get_size(self):
        return self.size

    def add_panel_item(self, panel_item):
        self.panel_items.append(panel_item)

    def add_balloon(self, balloon):
        self.balloons.append(balloon)

    def get_background(self):
        return self.panel_items[0]

    def get_panel_items(self):
        return self.characters + self.panel_items[1:]

    def add_character(self, character):
        self.characters.append(character)
