from Model.Character import Character
from Model.Position import Type, Position

POSITION_DEFAULT = Position((0, Type.AUTO), (0, Type.POURCENTAGE))
LEFT = Position((0, Type.POURCENTAGE), (0, Type.POURCENTAGE))
MIDDLE = Position((50, Type.POURCENTAGE), (0, Type.POURCENTAGE))
RIGHT = Position((100, Type.POURCENTAGE), (0, Type.POURCENTAGE))

IMAGE_DEFAULT = "sources/narrateur-angry.png"

class Name:
    name_counter = 0

    @staticmethod
    def new():
        Name.name_counter = Name.name_counter + 1
        return "Keno" + str(Name.name_counter)

class NewCharacter:

    def __init__(self):
        self._name = Name.new()
        self._position = POSITION_DEFAULT
        self._image = IMAGE_DEFAULT

    def named(self, name):
        self._name = name
        return self

    def at(self, position):
        self._position = position
        return self

    def create(self):
        return Character(self._name, self._image, self._position)

def character():
    return NewCharacter().create()

def character_named(name):
    return NewCharacter().named(name).create()

def character_named_at(name, position):
    return NewCharacter().named(name).at(position).create()

def character_at(position):
    return NewCharacter().at(position).create()
