class MakefileCommand:

    @staticmethod
    def generatePositionCommand(panelItem, panel):
        parameters = ["./scripts/pos.sh $<"]
        position = panelItem.get_position()
        parameters.append(str(position[0]))
        parameters.append(str(position[1]))
        parameters.append(str(panel.get_width()))
        parameters.append(str(panel.get_height()))
        parameters.append("$@")
        return " ".join(parameters)
