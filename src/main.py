from Strip import *
from PanelItem import *
from Panel import *
from MakefileGenerator import *
from Balloon import *

def main():
	background = PanelItem("sources/background.png")
	bluePerso = PanelItem("sources/perso1.png")
	redPerso = PanelItem("sources/perso2.png")

	balloon1 = Balloon(["Hi !"], 40, (-50, -35), (350, 100))

	panelTop = Panel(1074, 768)
	panelMiddle = Panel(1074, 768)
	panelBottom = Panel(1074, 768)

	panelTop.addPanelItem(background)
	panelTop.addPanelItem(bluePerso)
	panelTop.addPanelItem(redPerso)
	panelTop.addBalloon(balloon1)

	panelMiddle.addPanelItem(background)
	panelMiddle.addPanelItem(redPerso)

	panelBottom.addPanelItem(background)
	panelBottom.addPanelItem(bluePerso)

	strip = Strip()
	strip.addPanel(panelTop)
	strip.addPanel(panelMiddle)
	strip.addPanel(panelBottom)

	makefileGenerator = MakefileGenerator(strip, "results")
	makefileGenerator.generateMakefile()

main()
