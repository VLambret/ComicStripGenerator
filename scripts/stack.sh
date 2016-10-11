#!/bin/bash

function usage {
	echo "stack.sh img1 img2 [...] output.png"
	echo "        compose several images by stacking from background to foreground"
}

if [ 3 -gt $# ]; then
	echo "Illegal number of parameters"
	usage
	exit -1
fi

eval "OUTPUT=\${$#}"

length=$(($#-3))
array=(${@:3:$length})

composite $2 $1 ${OUTPUT}

for i in "${array[@]}"
do
	composite $i ${OUTPUT} ${OUTPUT}
done
