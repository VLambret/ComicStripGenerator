class Panel:

    def __init__(self, background_panel_item):
        self._background_size = background_panel_item.get_size()
        self._panel_item_list = []
        self._balloon_list = []
        self.add_panel_item(background_panel_item)

    def add_panel_item(self, panel_item):
        self._panel_item_list.append(panel_item)

    def add_balloon(self, balloon):
        self._balloon_list.append(balloon)

    def get_width(self):
        return self._background_size[0]

    def get_height(self):
        return self._background_size[1]

    def get_panel_items(self):
        for item in self._panel_item_list:
            yield item

    def get_balloons(self):
        for balloon in self._balloon_list:
            yield balloon
