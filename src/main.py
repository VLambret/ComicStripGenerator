from Strip import *
from PanelItem import *
from Panel import *

def main():
	background = PanelItem("../sources/background.png")
	bluePerso = PanelItem("../sources/perso1.png")
	redPerso = PanelItem("../sources/perso2.png")

	panelTop = Panel(1074)
	panelMiddle = Panel(1074)
	panelBottom = Panel(1074)

	panelTop.addPanelItem(background)
	panelTop.addPanelItem(bluePerso)
	panelTop.addPanelItem(redPerso)

	panelMiddle.addPanelItem(background)
	panelMiddle.addPanelItem(redPerso)

	panelBottom.addPanelItem(background)
	panelBottom.addPanelItem(bluePerso)

	strip = Strip()
	strip.addPanel(panelTop)
	strip.addPanel(panelMiddle)
	strip.addPanel(panelBottom)

main()
