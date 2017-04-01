from Strip import *
from PanelItem import *
from Panel import *
from MakefileGenerator import *
from Balloon import *
import argparse

def createPanelFromBackground(config):
    backgroundFileName = PanelItem("sources/"+ config[1], (0, 0))
    return Panel(backgroundFileName)

def createItem(panel, config):
    item = PanelItem("sources/"+ config[1], (config[2], config[3]))
    panel.add_panel_item(item)

# balloon:350:100:40:-50:-35:"Hi !"
def createBalloon(panel, config):
    speeches = config[6]
    position=(config[1], config[2])
    offset=config[3]
    orientation=(config[4], config[5])
    balloon = Balloon(speeches, offset, orientation, position)
    panel.add_balloon(balloon)

def initFromFile(fileName):
    strip = Strip()
    panel = None

    with open(fileName, 'r') as f:
        for line in f:
            parsedLine = line.rstrip().split(':')
            typeOfItem = parsedLine[0]

            print("#^" +typeOfItem + "$")

            if typeOfItem == "background":
                if panel is not None:
                    strip.addPanel(panel)
                panel = createPanelFromBackground(parsedLine)
            elif typeOfItem == "item":
                createItem(panel, parsedLine)
            elif typeOfItem == "balloon":
                createBalloon(panel, parsedLine)
        strip.addPanel(panel)
    return strip

def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', help = "comic file to transform into Makefile", default = "strip.comic", type = str, required = False)
    parser.add_argument('-w', help = "workdir where temporary files are created", default = "results", type = str, required = False)
    args = parser.parse_args()
    return args.f, args.w

def main():
    comicFileName, workDir = getArgs()
    finalPNGName = comicFileName.replace(".comic", ".png")
    strip = initFromFile(comicFileName)
    makefileGenerator = MakefileGenerator(strip, finalPNGName, workDir)
    makefileGenerator.generateMakefile()

main()
