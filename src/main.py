from Strip import *
from PanelItem import *
from Panel import *
from MakefileGenerator import *
from Balloon import *

def createBackground(panel, config):
    background = PanelItem("sources/"+ config[1], (0, 0))
    panel.addPanelItem(background)

def createItem(panel, config):
    item = PanelItem("sources/"+ config[1], (config[2], config[3]))
    panel.addPanelItem(item)

# balloon:350:100:40:-50:-35:"Hi !"
def createBalloon(panel, config):
    speeches = config[6]
    position=(config[1], config[2])
    offset=config[3]
    orientation=(config[4], config[5])
    balloon = Balloon(speeches, offset, orientation, position)
    panel.addBalloon(balloon)

def initFromFile(fileName):
    strip = Strip()
    panel = Panel(1024, 768)

    with open(fileName, 'r') as f:
        for line in f:
            parsedLine = line.rstrip().split(':')
            typeOfItem = parsedLine[0]

            print("#^" +typeOfItem + "$")

            if typeOfItem == "background":
                createBackground(panel, parsedLine)
            elif typeOfItem == "item":
                createItem(panel, parsedLine)
            elif typeOfItem == "balloon":
                createBalloon(panel, parsedLine)
            elif typeOfItem == "":
                strip.addPanel(panel)
                panel = Panel(1024, 768)
        strip.addPanel(panel)
    return strip

def main():
	strip = initFromFile("strip.comic")
	makefileGenerator = MakefileGenerator(strip, "results")
	makefileGenerator.generateMakefile()

main()
