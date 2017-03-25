class MakefileGenerator():

	def __init__(self, strip, workDir):
		self.strip = strip
		self.workDir = workDir

	def generatePanelRules(self):
		pass

	def generateStripRule(self):
		target = self.workDir + "/strip.png"

		dependancies = []
		i = 1
		for panel in self.strip.panelList:
			dependancies.append(self.workDir + "/panel" + str(i) + ".png")
			i += 1

		commands = ["convert -append $^ $@"]

		self.printMakefileRule(target, dependancies, commands)

	def generateMakefile(self):
		self.generateStripRule()
		self.generatePanelRules()

	def printMakefileRule(self, target, dependancies, commands):
		print(target + " : ", end = "")
		dependancyIndentation = " " * (len(target) + 3)
		first = True
		dependanciesNumber = len(dependancies)
		counter = 0
		for d in dependancies:
			if first:
				first = False
			else:
				print(dependancyIndentation, end="")
			print(d + " ", end="")

			counter += 1
			if counter != dependanciesNumber:
				print(" \\")
		print()
		for c in commands:
			print("\t" + c)
