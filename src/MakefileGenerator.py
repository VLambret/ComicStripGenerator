from Makefile import Makefile

class MakefileGenerator():

    def __init__(self, strip, png_target_name, work_dir):
        self._strip = strip
        self._png_target_name = png_target_name
        self._work_dir = work_dir

    def generate_panel_balloon_rules(self, panel, panel_counter):
        balloon_counter = 0

        for balloon in panel.get_balloons():
            target_prefix = self._work_dir + "/panel" + str(panel_counter)
            target_prefix += "_balloon" + str(balloon_counter)
            target_pos_name = target_prefix + "_pos.png"
            target_name = target_prefix + ".png"
            target_svg_name = target_prefix + ".svg"

            pos_command = Makefile.generate_position_command(balloon, panel)

            svg_command = "./scripts/balloon.py -x 0 -y 0 -offset " + balloon.get_offset()
            svg_command += " -bx " + balloon.get_horizontal_orientation()
            svg_command += "  -by " + balloon.get_vertical_orientation()
            svg_command += " -c " + balloon.get_speech() + " > $@"

            Makefile.print_makefile_rule(target_pos_name, [target_name], [pos_command])
            Makefile.print_makefile_rule(target_svg_name, [""], [svg_command])

            balloon_counter += 1

    def generate_panel_rules(self):
        panel_counter = 0

        convert_command = "convert $@ -bordercolor black -compose Copy -border 5"
        convert_command += " -bordercolor white -compose Copy -border 20 $@"
        commands = ["./scripts/stack.sh $^ $@", convert_command]

        for panel in self._strip:
            target = self._work_dir + "/panel" + str(panel_counter) + ".png"

            dependancies = []
            item_counter = 1
            for panel_item in panel.get_panel_items():
                item_pos_rule_name = target.replace(".png", "_pos" + str(item_counter) + ".png")
                dependancies.append(item_pos_rule_name)

                Makefile.generate_pos_item_rule(item_pos_rule_name, panel_item, panel)

                item_counter += 1

            for balloon_counter in range(0, panel.get_balloons_number()):
                dependancy = self._work_dir + "/panel" + str(panel_counter)
                dependancy += "_balloon" + str(balloon_counter) + "_pos.png"
                dependancies.append(dependancy)

            self.generate_panel_balloon_rules(panel, panel_counter)

            Makefile.print_makefile_rule(target, dependancies, commands)
            panel_counter += 1

    def generate_strip_rule(self):
        dependancies = []
        for panel_counter in range(0, len(self._strip)):
            dependancies.append(self._work_dir + "/panel" + str(panel_counter) + ".png")

        commands = ["convert -append $^ $@"]

        Makefile.print_makefile_rule(self._png_target_name, dependancies, commands)

    def generate_makefile(self):
        Makefile.print_generic_rules()
        self.generate_strip_rule()
        self.generate_panel_rules()
