class sentence:


    def __init__(self, filename):
        with open(filename) as f:
            self.lines = f.read().splitlines()
            f.close()

    # Return max line width
    def width(self):
        return max(len(str(x)) for x in self.lines)

    # Return number of lines
    def height(self):
        return len(self.lines)

    def getLines(self):
        return self.lines

    def toSVG():
            line = "<line x1=\"{}\" y1=\"{}\" x2=\"{}\" y2=\"{}\" style=\"stroke:black;stroke-width:10\" />\n".format(c.x, c.y, p.x, p.y)
        "<rect x=\"2.5\" y=\"2.5\" rx=\"30\" ry=\"30\" width=\"295\" height=\"95\" fill=\"#e7e7e7\""
        "style=\"fill:#ffffff;"
        "fill-opacity:1;"
        "fill-rule:nonzero;"
        "stroke:#1a1a1a;"
        "stroke-width:5;"
        "stroke-linecap:butt;"
        "stroke-linejoin:round;"
        "stroke-miterlimit:0;"
        "stroke-opacity:1;"
        "stroke-dasharray:none;"
        "stroke-dashoffset:0\" ></rect>"


