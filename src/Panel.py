class Panel:

    def __init__(self, background_panel_item):
        self.background_size = background_panel_item.getSize()
        self.panel_item_list = []
        self.balloon_list = []
        self.add_panel_item(background_panel_item)

    def add_panel_item(self, panel_item):
        self.panel_item_list.append(panel_item)

    def add_balloon(self, balloon):
        self.balloon_list.append(balloon)

    def get_width(self):
        return self.background_size[0]

    def get_height(self):
        return self.background_size[1]

    def get_panel_items(self):
        for item in self.panel_item_list:
            yield item

    def get_balloons(self):
        for balloon in self.balloon_list:
            yield balloon
