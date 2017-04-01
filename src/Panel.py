from PanelItem import *

class Panel:

    def __init__(self, backgroundPanelItem):
        backgroundSize = backgroundPanelItem.getSize()
        self.panelItemList = []
        self.balloonList = []
        self.width = backgroundSize[0]
        self.height= backgroundSize[1]
        self.addPanelItem(backgroundPanelItem)

    def addPanelItem(self, panelItem):
        self.panelItemList.append(panelItem)

    def addBalloon(self, balloon):
        self.balloonList.append(balloon)
