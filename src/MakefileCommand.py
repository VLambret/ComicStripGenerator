class MakefileCommand:

    @staticmethod
    def generate_position_command(panel_item, panel):
        parameters = ["./scripts/pos.sh $<"]
        position = panel_item.get_position()
        parameters.append(str(position[0]))
        parameters.append(str(position[1]))
        parameters.append(str(panel.get_width()))
        parameters.append(str(panel.get_height()))
        parameters.append("$@")
        return " ".join(parameters)
