from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

border = 40

def drawBalloon(speech):
	im = Image.new("RGB", (1, 1), "white")
	draw = ImageDraw.Draw(im)
	fontsize = 70
	font = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", fontsize)
	x, y = (draw.textsize(speech, font=font))

	size = (x + border, y + border)
	im = Image.new("RGB", (size), "white")
	draw = ImageDraw.Draw(im)
	draw.rectangle([(0, 0), size], fill="white", outline="black")
	draw.text((20, 20), speech, fill="black", font = font)

	im.show()

drawBalloon("Hello World!")
