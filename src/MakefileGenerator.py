from MakefileCommand import *

class MakefileGenerator():

    def __init__(self, strip, pngTargetName, workDir):
        self.strip = strip
        self.pngTargetName = pngTargetName
        self.workDir = workDir

    def generatePanelBalloonsRules(self, panel, panelCounter):
        balloonCounter = 1

        for balloon in panel.get_balloons():
            targetPrefix = self.workDir + "/panel" + str(panelCounter) + "_balloon" + str(balloonCounter)
            targetPosName = targetPrefix + "_pos.png"
            targetName = targetPrefix + ".png"
            targetSVGName = targetPrefix + ".svg"

            posCommand = MakefileCommand.generatePositionCommand(balloon ,panel)

            svgCommand = "./scripts/balloon.py -x 0 -y 0 -offset " + str(balloon.offset) +  " -bx " + str(balloon.orientation[0]) + "  -by " + str(balloon.orientation[1]) + " -c " + balloon.speech + " > $@"

            self.printMakefileRule(targetPosName, [targetName], [posCommand])
            self.printMakefileRule(targetSVGName, [""], [svgCommand])

            balloonCounter += 1

    def generatePosItemRule(self, targetName, panelItem, panel):
        posCommand = MakefileCommand.generatePositionCommand(panelItem ,panel)
        self.printMakefileRule(targetName, [panelItem.get_image_name()], [posCommand])

    def generatePanelRules(self):
        panelCounter = 1

        commands = ["./scripts/stack.sh $^ $@", "convert $@ -bordercolor black -compose Copy -border 5 -bordercolor white -compose Copy -border 20 $@"]

        for panel in self.strip:
            target = self.workDir + "/panel" + str(panelCounter) + ".png"

            dependancies = []
            itemCounter = 1
            for panelItem in panel.get_panel_items():
                itemPosRuleName = target.replace(".png", "_pos" + str(itemCounter) + ".png")
                dependancies.append(itemPosRuleName)

                self.generatePosItemRule(itemPosRuleName, panelItem, panel)

                itemCounter += 1

            balloonCounter = 1
            for balloon in panel.get_balloons():
                dependancies.append(self.workDir + "/panel" + str(panelCounter) + "_balloon" + str(balloonCounter) + "_pos.png")
                balloonCounter += 1

            self.generatePanelBalloonsRules(panel, panelCounter)

            self.printMakefileRule(target, dependancies, commands)
            panelCounter += 1

    def generateStripRule(self):
        dependancies = []
        i = 1
        for panel in self.strip:
            dependancies.append(self.workDir + "/panel" + str(i) + ".png")
            i += 1

        commands = ["convert -append $^ $@"]

        self.printMakefileRule(self.pngTargetName, dependancies, commands)

    def generateMakefile(self):
        self.printGenericRules()
        self.generateStripRule()
        self.generatePanelRules()

    def printMakefileRule(self, target, dependancies, commands):
        print(target + " : ", end = "")
        dependancyIndentation = " " * (len(target) + 3)
        first = True
        dependanciesNumber = len(dependancies)
        counter = 0
        for d in dependancies:
            if first:
                first = False
            else:
                print(dependancyIndentation, end="")
            print(d + " ", end="")

            counter += 1
            if counter != dependanciesNumber:
                print(" \\")
        print()
        for c in commands:
            print("\t" + c)
        print()

    def printGenericRules(self):
        self.printMakefileRule("%.png", ["%.svg"], ["convert $< $@"])
