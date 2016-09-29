import argparse

output_file = "../sources/speechballoontest.svg"

def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('-x', type = float, required = True)
	parser.add_argument('-y', type = float, required = True)
	parser.add_argument('-dx', type = float, required = True)
	parser.add_argument('-dy', type = float, required = True)
	parser.add_argument('-c', type = str, required = True)
	args = parser.parse_args()
	return args.x, args.y, args.dx, args.dy, args.c

def output_balloon(output_file, x, y, dx, dy, c):
	f = open(output_file, "w")
	header = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- -->

<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   width="210mm"
   height="297mm"
   id="svg2"
   version="1.1"
   inkscape:version="0.48.5 r10040"
   sodipodi:docname="Nouveau document 1">
  <defs
     id="defs4" />
  <sodipodi:namedview
     id="base"
     pagecolor="#ffffff"
     bordercolor="#666666"
     borderopacity="1.0"
     inkscape:pageopacity="0"
     inkscape:pageshadow="2"
     inkscape:zoom="3.959798"
     inkscape:cx="236.78571"
     inkscape:cy="631.11678"
     inkscape:document-units="px"
     inkscape:current-layer="layer1"
     showgrid="false"
     inkscape:window-width="1918"
     inkscape:window-height="1169"
     inkscape:window-x="0"
     inkscape:window-y="0"
     inkscape:window-maximized="0" />
  <metadata
     id="metadata7">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type
           rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
        <dc:title></dc:title>
      </cc:Work>
    </rdf:RDF>
  </metadata>
"""
	rect = """	<rect
		style="fill:#ffffff;fill-opacity:1;fill-rule:nonzero;stroke:#1a1a1a;stroke-width:5;stroke-linecap:butt;stroke-linejoin:round;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;stroke-dashoffset:0"
		id="balloon"
		width=""" + "\"" + str(dx) + "\"" + """
		height=""" + "\"" + str(dy) + "\"" + """
		x=""" + "\"" + str(x) + "\"" + """
		y=""" + "\"" + str(y) + "\"" + """
		ry="17.857147"
	/>
"""
	hide = """	<rect
	style="fill:#ffffff;fill-opacity:1;fill-rule:nonzero;stroke:#ffffff;stroke-width:0;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;stroke-dashoffset:0"
	id="hide"
	width="20.46574"
	height="30.052038"
	x=""" + "\"" + str(dx/3 + x) + "\"" + """
	y=""" + "\"" + str(y + dy - 28.052038) + "\"" + """
	/>
"""

	path = """	<path
	style="fill:#ffffff;fill-opacity:1;fill-rule:nonzero;stroke:#1a1a1a;stroke-width:5;stroke-linecap:butt;stroke-linejoin:round;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;stroke-dashoffset:0"
	d="m """ + str(x + dx/3 - 0.8) + "," + str(y + dy - 2.45) + """ -0.1177,11.13567 -11.24652,17.65368 34.37565,-26.78428"
	id="peak"
	inkscape:connector-curvature="0"
	sodipodi:nodetypes="cccc" />
"""

	text = """	<text
	style="font-size:40px;font-style:normal;font-variant:normal;font-weight:500;font-stretch:normal;text-align:center;line-height:125%;letter-spacing:0px;word-spacing:0px;text-anchor:middle;fill:black;opacity:1;stroke:none;font-family:OpenComicFont;-inkscape-font-specification:OpenComicFont Medium"
	x=""" + "\"" + str(x + dx/2) + "\"" + """
	y=""" + "\"" + str(y + dy/2 + 10) + "\"" + """
	alignment-baseline="middle"
	text-anchor="middle"
	>""" + c + """</text>
"""

	body = """ <g
     inkscape:label="Calque 1"
     inkscape:groupmode="layer"
     id="layer1">

	<!-- Balloon -->
	<!-- ry : define the corners round -->
	<g inkscape:label="Balloon"
	   inkscape:groupmode="layer"
	   id="layer2">
""" + rect + hide + path + """</g>
	<!-- Text -->
""" + text + """
</g>
</svg>
"""
	f.write(header + body)
	f.close()

x, y, dx, dy, c = get_args()
output_balloon(output_file, x, y, dx, dy, c)
