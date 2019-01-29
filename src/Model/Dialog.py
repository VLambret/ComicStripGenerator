class Dialog:

    def __init__(self, name, speech):
        self.name = name
        self.speech = speech

    def __repr__(self):
        return "name: {0}, speech: {1}".format(self.name, self.speech)
