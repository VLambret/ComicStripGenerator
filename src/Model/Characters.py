
class Characters:

    def __init__(self):
        self._characters = []
        pass

    def add(self, character):
        self._characters.append(character)

    def get_items(self):
        return self._characters