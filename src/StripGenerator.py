import math
from PIL import Image
from PIL import ImageDraw
from PIL import ImageOps
import ImageFactory

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

def add_borders(image, size, color):
    return ImageOps.expand(image, size, color)

def create_image_from_panel(panel):
    panel_image = create_image_from_background(panel.get_background())
    return overlay_panel_items(panel_image, panel.get_panel_items())

def draw_tail(draw, position, size, angle, length):
    start = (position[0] + size[0] / 2, position[1] + size[1])
    offsetx = length * math.cos(math.radians(angle))
    offsety = length * math.sin(math.radians(angle))
    end = (start[0] + offsetx, start[1] + offsety)
    draw.line([start, end], fill="black", width=6)

def overlay_balloons_to_panel(panel_image, balloons):
    balloons_image = Image.new("RGBA", panel_image.size, (0, 0, 0, 0))
    tails_image = Image.new("RGBA", panel_image.size, (0, 0, 0, 0))
    tail_draw = ImageDraw.Draw(tails_image)

    for balloon in balloons:
        font_name = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
        balloon_text = ImageFactory.draw_balloon_text(balloon.speech, font_name, 40)
        balloon_image = ImageFactory.draw_balloon(balloon_text, 25, 6)
        balloons_image.paste(balloon_image, balloon.position)
        draw_tail(tail_draw, balloon.position, balloon_image.size,
                  balloon.tail_angle, balloon.tail_length)
        # XXX
    complete_balloon_image = Image.alpha_composite(tails_image, balloons_image)
    return Image.alpha_composite(panel_image, complete_balloon_image)

def create_image_from_strip(strip, output_file_name):
    strip_width = 0
    strip_height = strip.space_arround_panels
    panel_image_list = []
    for panel in strip.panels:
        panel_image = create_image_from_panel(panel)
        panel_image = add_borders(panel_image,
                                  strip.panel_border_size,
                                  strip.panel_border_color)
        panel_image = overlay_balloons_to_panel(panel_image, panel.balloons)
        strip_width = max(strip_width, panel_image.size[0])
        strip_height += panel_image.size[1] + strip.space_arround_panels
        panel_image_list.append(panel_image)

    strip_width += 2* strip.space_arround_panels

    strip_image = Image.new("RGBA", (strip_width, strip_height), strip.background_color)

    height_offset = strip.space_arround_panels
    for panel_image in panel_image_list:
        strip_image.paste(panel_image, (strip.space_arround_panels, height_offset))
        height_offset += panel_image.size[1] + strip.space_arround_panels

    strip_image.save(output_file_name, "PNG")
