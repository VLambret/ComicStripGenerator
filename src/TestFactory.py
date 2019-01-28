from Model.Character import Character
from Model.Position import Type, Position

POSITION_DEFAULT = Position((0, Type.AUTO), (0, Type.POURCENTAGE))

def character():
    return character_named("Keno")

def character_named(name):
    return Character(name, "sources/narrateur-angry.png", POSITION_DEFAULT)
