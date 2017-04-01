class MakefileCommand:

    @staticmethod
    def generatePositionCommand(panelItem, panel):
        parameters = ["./scripts/pos.sh $<"]
        parameters.append(str(panelItem.position[0]))
        parameters.append(str(panelItem.position[1]))
        parameters.append(str(panel.width))
        parameters.append(str(panel.height))
        parameters.append("$@")
        return " ".join(parameters)
