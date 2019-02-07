from Model.Config import Config

class Strip:

    def __init__(self):
        self.background_color = "white"
        self.space_arround_panels = 25
        self.config = Config()
        self.panels = []

    def last_panel(self):
        return self.panels[-1]
