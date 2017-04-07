from PIL import Image
from PIL import ImageOps

def create_image_from_background(background):
    return Image.open(background.get_image_name())

def overlay_panel_items(image, panel_items):
    for panel_item in panel_items:
        item_position = panel_item.get_position()
        item_image = Image.open(panel_item.get_image_name())

        image.paste(item_image, item_position)

def draw_borders(image):
    return ImageOps.expand(image, 5, "black")

def create_image_from_panel(panel):
    panel_image = create_image_from_background(panel.get_background())
    overlay_panel_items(panel_image, panel.get_panel_items())
    return draw_borders(panel_image)

def create_image_from_strip(strip):
    strip_width = 0
    strip_height = 0
    panel_image_list = []
    for panel in strip:
        panel_image = create_image_from_panel(panel)
        strip_width = max(strip_width, panel_image.size[0])
        strip_height+= panel_image.size[1]
        panel_image_list.append(panel_image)

    strip_image = Image.new("RGBA", (strip_width, strip_height), "white")

    print("width=" + str(strip_width) + ", height=" + str(strip_height))

    height_offset = 0
    for panel_image in panel_image_list:
        strip_image.paste(panel_image, (0, height_offset))
        height_offset += panel_image.size[1]

    strip_image.show()

#perso = Image.new("RGB", (200, 400), "red")
#realPerso = Image.open("sources/narrateur-smiling.png")
#
#background.paste(perso, (400,368))
#background.paste(realPerso, (10,20))
#background.paste(realPerso, (100,200))
#background = ImageOps.expand(background, 5, "green")
#
#background.show()
