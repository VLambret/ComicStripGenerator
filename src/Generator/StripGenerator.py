from PIL import Image
from PIL import ImageDraw
from PIL import ImageOps

import Config
from Generator.PanelImage import PanelImage


def add_borders(image, size, color):
    return ImageOps.expand(image, size, color)

def reduce_tail_end(start, end):
    reduction = 70
    reduce_x = start[0] + (reduction * (end[0] - start[0])) / 100
    reduce_y = start[1] + (reduction * (end[1] - start[1])) / 100
    return reduce_x, reduce_y

def draw_tail(draw, position, balloon):
    start = balloon.get_tail_start_at(position)
    end = reduce_tail_end(start, balloon.get_tail_end())
    draw.line([start, end], fill="black", width=Config.border_width)

def overlay_balloons_to_panel(panel_image, balloons):
    balloons_image = Image.new("RGBA", panel_image.size, (0, 0, 0, 0))
    tails_image = Image.new("RGBA", panel_image.size, (0, 0, 0, 0))
    tail_draw = ImageDraw.Draw(tails_image)

    for balloon in balloons:
        tmp_image = Image.new("RGBA", panel_image.size, (0, 0, 0, 0))
        balloon_position = balloon.get_coordinates_in(panel_image)
        tmp_image.paste(balloon.image, balloon_position)
        draw_tail(tail_draw, balloon_position, balloon)
        balloons_image = Image.alpha_composite(balloons_image, tmp_image)

    complete_balloon_image = Image.alpha_composite(tails_image, balloons_image)
    return Image.alpha_composite(panel_image, complete_balloon_image)

def create_image_from_strip(strip, output_file_name):
    strip_width = 0
    strip_height = strip.space_arround_panels
    panel_image_list = []
    for panel in strip.panels:
        panel_image = PanelImage(panel).image
        panel_image = add_borders(panel_image,
                                  strip.config.border_size,
                                  strip.config.border_color)
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
