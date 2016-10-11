#!/bin/bash

function usage {
	echo "stack.sh img1 img2 [...] output.png"
	echo "        compose several images by stacking from background to foreground"
}

if [ 3 -gt $# ]; then
	echo "illegal number of parameters"
	usage
	exit -1
fi

length=$(($#-3))
array=(${@:3:$length})

composite $1 $2 ${@: -1}

for i in "${array[@]}"
do
	composite ${@: -1} $i ${@: -1}
done
