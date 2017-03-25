class Panel:

	def __init__(self, width):
		self.panelItemList = []
		self.width = width

	def addPanelItem(self, panelItem):
		self.panelItemList.append(panelItem)
