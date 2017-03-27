from PIL import Image

class PanelItem:

	def __init__(self, imageName, position):
		self.imageName = imageName
		im = Image.open(self.imageName)
		self.size = im.size
		self.position = position

	def getSize(self):
		return self.size
