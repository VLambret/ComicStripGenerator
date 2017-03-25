class Panel:

	def __init__(self, width, height):
		self.panelItemList = []
		self.balloonList = []
		self.width = width
		self.height= height

	def addPanelItem(self, panelItem):
		self.panelItemList.append(panelItem)

	def addBalloon(self, balloon):
		self.balloonList.append(balloon)
