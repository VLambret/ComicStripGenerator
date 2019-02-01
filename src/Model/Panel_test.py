import pytest

from Model.Panel import Panel
from Model.Position import Type
from Model.Position import Position
from Model.Character import Character
import Config

DEFAULT_BACKGROUND = "background.png"
DEFAULT_IMAGE = Config.image_database+"/narrateur-smiling.png"

def test_panel_instance():
    panel = Panel(DEFAULT_BACKGROUND)
