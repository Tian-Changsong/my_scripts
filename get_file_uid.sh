#!/bin/bash --noprofile
realpath=`readlink -m $1`
unicode=(`echo $realpath | md5sum`)
echo ${unicode[0]}
