from Model.PanelItem import PanelItem

class Character(PanelItem):

    def __init__(self, name, image_name, position):
        super().__init__(image_name, position)
        self.name = name
