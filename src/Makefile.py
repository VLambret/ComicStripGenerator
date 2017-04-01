class Makefile:

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

    @staticmethod
    def print_makefile_rule(target, dependancies, commands):
        print(target + " : ", end="")
        dependancy_indentation = " " * (len(target) + 3)
        first = True
        dependancies_number = len(dependancies)
        counter = 0
        for dependancy in dependancies:
            if first:
                first = False
            else:
                print(dependancy_indentation, end="")
            print(dependancy + " ", end="")

            counter += 1
            if counter != dependancies_number:
                print(" \\")
        print()
        for command in commands:
            print("\t" + command)
        print()

    @staticmethod
    def generate_pos_item_rule(target_name, panel_item, panel):
        pos_command = Makefile.generate_position_command(panel_item, panel)
        Makefile.print_makefile_rule(target_name, [panel_item.get_image_name()], [pos_command])

    @staticmethod
    def print_generic_rules():
        Makefile.print_makefile_rule("%.png", ["%.svg"], ["convert $< $@"])
