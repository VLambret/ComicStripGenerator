from commit import *

class svg_document:

    def __init__(self, prefix, width, height, background):
        self.prefix = prefix
        self.width = width
        self.height = height
        self.background = background
        self.number = 0

    def nextFile(self):
        filename = self.prefix +  "{0:08d}".format(self.number) + ".svg"
        self.number = self.number + 1
        return open(filename, 'w')

    def header(self, f):
        s = "<svg height=\"{}\" width=\"{}\">\n".format(self.height, self.width)
        f.write(s)

    def footer(self, f):
        s = "</svg>"
        f.write(s)

    def generate_links(self, commits, f):
        for tag in commits:
            c = commits[tag]
            if c.parent == "":
                continue
            p = commits[c.parent]
            line = "<line x1=\"{}\" y1=\"{}\" x2=\"{}\" y2=\"{}\" style=\"stroke:black;stroke-width:10\" />\n".format(c.x, c.y, p.x, p.y)
            f.write(line)

    def generate_commits(self, commits, f):
        for tag in commits:
            line = commits[tag].toSVG()
            f.write(line)
        
