from Model.Character import Character
from Model.Position import Type, Position

POSITION_DEFAULT = Position((0, Type.AUTO), (0, Type.POURCENTAGE))
LEFT = Position((0, Type.POURCENTAGE), (0, Type.POURCENTAGE))
MIDDLE = Position((50, Type.POURCENTAGE), (0, Type.POURCENTAGE))
RIGHT = Position((100, Type.POURCENTAGE), (0, Type.POURCENTAGE))

def character():
    return character_named("Keno")

def character_named(name):
    return Character(name, "sources/narrateur-angry.png", POSITION_DEFAULT)

def character_named_at(name, position):
    return Character(name, "sources/narrateur-angry.png", position)
