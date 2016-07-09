#! /bin/csh -f
set realpath=`readlink -m $1`
set unicode=`echo $realpath | md5sum`
echo $unicode[1]
