from PIL import Image


class PanelImage:

    def __init__(self, panel):
        self._panel_model = panel
        pass

    @property
    def image(self):
        panel_image = self._panel_model.background.image
        for panel_item in self._panel_model.get_panel_items():
            panel_image = overlay_item(panel_image, panel_item)
        return panel_image

def overlay_item(image, item):
    # PIL paste dont handle alpha, we have to use alpha_composite but it only
    #  accept images with the same size. The workarround here consist to create
    # a temporary alpha image where the panel_item is pasted at the correct
    #  position and then composite this image.
    alpha_tmp = Image.new('RGBA', image.size, (255, 255, 255, 0))
    alpha_tmp.paste(item.image, item.get_coordinates_in(image))
    return Image.alpha_composite(image, alpha_tmp)
