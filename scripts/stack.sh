#!/bin/bash

length=$(($#-3))
array=(${@:3:$length})

composite $1 $2 ${@: -1}

for i in "${array[@]}"
do
	composite ${@: -1} $i ${@: -1}
done
