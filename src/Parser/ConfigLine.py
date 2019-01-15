import Config

class ConfigLine:

    def __init__(self, line):
        self.config_key = line.rstrip().split(':')[0]
        self.value = line.rstrip().split(':')[1]

    def modify(self, strip):
        if self.config_key == "database":
            Config.image_database = self.value
