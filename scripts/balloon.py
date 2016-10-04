#!/usr/bin/python

import svg_generator
import argparse

FONTSIZE = 40
INTERLINE = FONTSIZE * 0.375
PADDING = FONTSIZE / 2

#Number of pixels for a standard character
WIDTH_CHAR = FONTSIZE * 3/4

#lists defining characters with small or medium width
small = ['.', ',', '\'', '!', ':', '\"', 'i', 'I', '|', '(', ')', '[', ']', '{', '}', '`', ';']
medium = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('-x', help = "top left absciss of the bubble", type = float, required = True)
	parser.add_argument('-y', help = "top left ordinate of the bubble", type = float, required = True)
	parser.add_argument('-offset', help = "Space before peak", type = float, required = True)
	parser.add_argument('-bx', help = "coordinate for the bubble orientation", type = float, required = True)
	parser.add_argument('-by', help = "coordinate for the bubble orientation", type = float, required = True)
	parser.add_argument('-c', help = "Text for the bubble", type = str, required = True, nargs ="+")
	args = parser.parse_args()
	return args.x, args.y, args.offset, args.bx, args.by, args.c

def orientation(o):
	if o != 'l' and o != 'r' :
		raise argparse.ArgumentTypeError("Orientation must be l or r")
	return o

#Generates svg for several lines of text
def multiline(x, y, w, h, c):
	result = ""
	i = 0
	while i < len(c) :
		result += svg_generator.text(x + w/2, y + (h / (len(c)+1)) + INTERLINE + i*FONTSIZE, w, h, c[i], FONTSIZE)
		i += 1
	return result

#Computes the height of the bubble according to the number of text lines
def height(c):
	h = len(c) * FONTSIZE + 2 * PADDING
	return h

#Computes the width needed for a word according to the width of its characters
def width_word(w):
	width = 0
	for letter in w :
		if letter in small :
			width += WIDTH_CHAR * 0.6
		elif letter in medium :
			width += WIDTH_CHAR * 0.8
		else :
			width += WIDTH_CHAR
	return width

#Computes the width of the bubble according to the largest word
def width(c):
	l = 0
	for w in c :
		width = width_word(w)
		if width > l :
			l = width
	return l + 2 * PADDING

def body(x, y, w, h, c, offset, bx, by):
	result = """ <g
     inkscape:label="Calque 1"
     inkscape:groupmode="layer"
     id="layer1">

	<!-- Balloon -->
	<!-- ry : define the corners round -->
	<g inkscape:label="Balloon"
	   inkscape:groupmode="layer"
	   id="layer2">
""" 
	result += svg_generator.rect(x, y, w, h)
	result += svg_generator.hide(x, y, w, h, offset)
	result += svg_generator.path(x, y, w, h, offset, bx, by)
	result += """</g>
	<!-- Text -->
""" 
	result += multiline(x, y, w, h, c)
	result +=  """
</g>
</svg>
"""
	return result

#Print svg for a speech balloon
def output_balloon(x, y, w, h, c, offset, bx, by):
	f = open("header.svg", 'r')
	print f.read()
	f.close()
	print body(x, y, w, h, c, offset, bx, by)

x, y, offset, bx, by, c = get_args()

h = height(c)
w = width(c)
output_balloon(x, y, w, h, c, offset, bx, by)
