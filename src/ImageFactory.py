from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def get_text_size(speech, font):
    image = Image.new("RGBA", (1, 1), "white")
    draw = ImageDraw.Draw(image)
    return draw.textsize(speech, font=font)

def center_text_images(text_images):
    width = 0
    height = 0
    for image in text_images:
        width = max(width, image.size[0])
        height = height + image.size[1]

    text_image_centered = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    offsety = 0
    for image in text_images:
        offsetx = (width - image.size[0]) // 2
        text_image_centered.paste(image, (offsetx, offsety))
        offsety += image.size[1]

    return text_image_centered

def draw_balloon_text(speech, font_name, font_size):
    font = ImageFont.truetype(font_name, font_size)
    text_images = []
    for text_line in speech.split('\n'):
        text_size = get_text_size(text_line, font)
        line_image = Image.new("RGBA", text_size, (0, 0, 0, 0))

        draw = ImageDraw.Draw(line_image)
        draw.text((0, 0), text_line, fill="black", font=font)
        text_images.append(line_image)

    return center_text_images(text_images)

def draw_lines(balloon_draw, text_size, padding, width):
    top_bottom = [(padding, 0),
                  (padding + text_size[0], 2 * padding + text_size[1])]
    top_bottom_inner = [(padding, width),
                        (padding + text_size[0], 2 * padding + text_size[1]-width)]
    left_right = [(0, padding),
                  (2 * padding + text_size[0], 1 * padding + text_size[1])]
    left_right_inner = [(width, padding),
                        (2 * padding + text_size[0] - width, 1 * padding + text_size[1])]

    balloon_draw.rectangle(top_bottom, fill="black", outline=None)
    balloon_draw.rectangle(top_bottom_inner, fill="white", outline=None)
    balloon_draw.rectangle(left_right, fill="black", outline=None)
    balloon_draw.rectangle(left_right_inner, fill="white", outline=None)

def orientation_to_offset_box(orientation, text_size):
    if orientation in [0, 270]:
        offsetx = text_size[0]
    else:
        offsetx = 0

    if orientation in [0, 90]:
        offsety = text_size[1]
    else:
        offsety = 0

    return (offsetx, offsety)

def draw_corners(balloon_draw, text_size, padding, width):
    for orientation in [0, 90, 180, 270]:
        offset_box = orientation_to_offset_box(orientation, text_size)
        color_box = [(0 + offset_box[0], 0 + offset_box[1]),
                     (2 * padding + offset_box[0], 2 * padding + offset_box[1])]
        white_box = [(width + offset_box[0], width + offset_box[1]),
                     (2 * padding - width + offset_box[0], 2 * padding - width + offset_box[1])]
        balloon_draw.pieslice(color_box, orientation, orientation + 90, "black")
        balloon_draw.pieslice(white_box, orientation, orientation + 90, "white")

def draw_balloon(balloon_text, padding, width):
    text_size = balloon_text.size
    balloon_size = (text_size[0] + 2 * padding, text_size[1] + 2 * padding)

    balloon = Image.new("RGBA", balloon_size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(balloon)

    draw_lines(draw, text_size, padding, width)
    draw_corners(draw, text_size, padding, width)

    balloon_text_padded = Image.new('RGBA', balloon_size, (255, 255, 255, 0))
    balloon_text_padded.paste(balloon_text, (padding, padding))

    return Image.alpha_composite(balloon, balloon_text_padded)

#speech = "Hello world, how\nare you today ?"
#font_name = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
#balloon_text = draw_balloon_text(speech, font_name, 40)
#balloon = draw_balloon(balloon_text, 25, 6)
#balloon.save("tmp.png", "PNG")
