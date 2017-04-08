from PIL import Image
from PIL import ImageOps

def create_image_from_background(background):
    return Image.open(background.get_image_name())

def overlay_panel_items(image, panel_items):
    for panel_item in panel_items:
        item_position = panel_item.get_position()
        item_image = Image.open(panel_item.get_image_name())

        # PIL paste dont handle alpha, we have to use alpha_composite but it only
        # accept images with the same size. The workarround here consist to create
        # a temporary alpha image where the panel_item is pasted at the correct
        # position and then composite this image.
        alpha_tmp = Image.new('RGBA', image.size, (255, 255, 255, 0))
        alpha_tmp.paste(item_image, item_position)
        image = Image.alpha_composite(image, alpha_tmp)
    return image

def draw_borders(image):
    return ImageOps.expand(image, 5, "black")

def create_image_from_panel(panel):
    panel_image = create_image_from_background(panel.get_background())
    panel_image = overlay_panel_items(panel_image, panel.get_panel_items())
    return draw_borders(panel_image)

def create_image_from_strip(strip, output_file_name):
    strip_width = 0
    strip_height = 0
    panel_image_list = []
    for panel in strip:
        panel_image = create_image_from_panel(panel)
        strip_width = max(strip_width, panel_image.size[0])
        strip_height += panel_image.size[1]
        panel_image_list.append(panel_image)

    strip_image = Image.new("RGBA", (strip_width, strip_height), "white")

    print("width=" + str(strip_width) + ", height=" + str(strip_height))

    height_offset = 0
    for panel_image in panel_image_list:
        strip_image.paste(panel_image, (0, height_offset))
        height_offset += panel_image.size[1]

    strip_image.save(output_file_name, "PNG")
