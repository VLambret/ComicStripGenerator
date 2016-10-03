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
def path(x, y, w, h, o):

	top_width = 23
	total_width = 34
	total_height = 28
	top_height = 11

	start_x = x + w/3 - 0.8
	start_y = y + h - 2.45

	if o == 'r':
		start_x += top_width 
		point3_x = total_width - top_width
		point4_x = -(total_width + 0.5)
	else :
		point3_x = -(total_width - top_width)
		point4_x = total_width + 0.5

	point1 = (start_x, start_y)
	point2 = (0, top_height)
	point3 = (point3_x, total_height - top_height)
	point4 = (point4_x, -total_height + 2)

	return """	<path
	style="fill:#ffffff;fill-opacity:1;fill-rule:nonzero;stroke:#1a1a1a;stroke-width:5;stroke-linecap:butt;stroke-linejoin:round;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;stroke-dashoffset:0"
	id="peak"
	d="m """ + str(point1[0]) +"," + str(point1[1]) + " " + str(point2[0]) + "," + str(point2[1]) + " " + str(point3[0]) + "," + str(point3[1]) + " " + str(point4[0]) + "," + str(point4[1]) + "\"" + """
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
