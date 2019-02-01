import Config
from Model.Panel import Panel

DEFAULT_BACKGROUND = "background.png"
DEFAULT_IMAGE = Config.image_database+"/narrateur-smiling.png"

def test_panel_instance():
    panel = Panel(DEFAULT_BACKGROUND)
    assert panel is not None
