class Panel:

    def __init__(self, background_panel_item):
        self.background = background_panel_item
        self.characters = []
        self.balloons = []

    @property
    def size(self):
        return self.background.get_size()

    def add_balloon(self, balloon):
        self.balloons.append(balloon)

    def get_panel_items(self):
        return self.characters

    def add_character(self, character):
        self.characters.append(character)
