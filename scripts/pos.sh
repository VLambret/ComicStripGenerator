#!/bin/bash

convert -size $4x$5 canvas:none -alpha transparent $6
composite -geometry +$2+$3 $1 $6 $6
