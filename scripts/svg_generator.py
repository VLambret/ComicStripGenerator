#Return svg for the main rectangle bubble
def rect(x, y, w, h):
	return """	<rect
		style="fill:#ffffff;fill-opacity:1;fill-rule:nonzero;stroke:#1a1a1a;stroke-width:5;stroke-linecap:butt;stroke-linejoin:round;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;stroke-dashoffset:0"
		id="balloon"
		width=""" + "\"" + str(w) + "\"" + """
		height=""" + "\"" + str(h) + "\"" + """
		x=""" + "\"" + str(x) + "\"" + """
		y=""" + "\"" + str(y) + "\"" + """
		ry="17.857147"
	/>
"""

#Return svg for the small rectangle hiding the top of the path
def hide(x, y , w, h):
	return """	<rect
	style="fill:#ffffff;fill-opacity:1;fill-rule:nonzero;stroke:#ffffff;stroke-width:0;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;stroke-dashoffset:0"
	id="hide"
	width="20.46574"
	height="30.052038"
	x=""" + "\"" + str(w/3 + x) + "\"" + """
	y=""" + "\"" + str(y + h - 28.052038) + "\"" + """
	/>
"""

#Return svg for the path (=peak of the bubble)
def path(x, y, w, h):
	return """	<path
	style="fill:#ffffff;fill-opacity:1;fill-rule:nonzero;stroke:#1a1a1a;stroke-width:5;stroke-linecap:butt;stroke-linejoin:round;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;stroke-dashoffset:0"
	d="m """ + str(x + w/3 - 0.8) + "," + str(y + h - 2.45) + """ -0.1177,11.13567 -11.24652,17.65368 34.37565,-26.78428"
	id="peak"
	inkscape:connector-curvature="0"
	sodipodi:nodetypes="cccc" />
"""

#Return svg for the text
def text(x, y, w, h, c, font_size):
	t = """	<text
	style="font-size:""" + str(font_size) + """px;font-style:normal;font-variant:normal;font-weight:500;font-stretch:normal;text-align:center;line-height:125%;letter-spacing:0px;word-spacing:0px;text-anchor:middle;fill:black;opacity:1;stroke:none;font-family:OpenComicFont;-inkscape-font-specification:OpenComicFont Medium"
	x=""" + "\"" + str(x) + "\"" + """
	y=""" + "\"" + str(y) + "\"" + """
	alignment-baseline="middle"
	text-anchor="middle"
	>"""
	t += c +"""</text>
"""
	return t
