from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def draw_balloon(speech, border, font):
    image = Image.new("RGB", (1, 1), "white")
    draw = ImageDraw.Draw(image)
    fontsize = 70
    font = ImageFont.truetype(font, fontsize)
    width, height = (draw.textsize(speech, font=font))

    size = (width + border, height + border)
    image = Image.new("RGB", (size), "white")
    draw = ImageDraw.Draw(image)
    draw.rectangle([(0, 0), size], fill="white", outline="black")
    draw.text((20, 20), speech, fill="black", font=font)

    image.show()

draw_balloon("Hello World!", 40, "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf")
