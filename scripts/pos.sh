#!/bin/bash

function usage {
	echo "pos.sh img x y width height output"
	echo "        place an image at (x,y) offset in a (width x height) transparent image"
}

if [ 6 != $# ]; then
	echo "Illegal number of parameters"
	usage
	exit -1
fi

SOURCE=$1
X=$2
Y=$3
WIDTH=$4
HEIGHT=$5
OUTPUT=$6

convert -size ${WIDTH}x${HEIGHT} canvas:none -alpha transparent $OUTPUT
composite -geometry +${X}+${Y} $SOURCE $OUTPUT $OUTPUT
