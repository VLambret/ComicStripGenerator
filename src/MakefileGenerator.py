class MakefileGenerator():

	def __init__(self, strip):
		self.strip = strip

	def generatePanelRules(self):
		pass

	def generateStripRule(self):
		pass

	def generateMakefile(self):
		self.generateStripRule()
		self.generatePanelRules()

