class MakefileCommand:

    @staticmethod
    def generatePositionCommand(panelItem, panel):
        parameters = ["./scripts/pos.sh $<"]
        parameters.append(str(panelItem.position[0]))
        parameters.append(str(panelItem.position[1]))
        parameters.append(str(panel.get_width()))
        parameters.append(str(panel.get_height()))
        parameters.append("$@")
        return " ".join(parameters)
