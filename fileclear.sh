#!/bin/bash

# inputs:
# "dir" -> the directory you wish to clear

function fileclear() {

ARGS=1 #we can only have 1 argument in this script

if [ $# -ne "$ARGS"  ]
then
	echo "Please only pass one argument"
	exit 
fi

if [ -d "$1" ]
then
	cd "$1"
	
	# if empty
	if [[ $(ls -A | wc -l) -eq 0 ]]
	then
		echo 'empty directory'
		exit 999
	fi
	
	files=$(ls -l | wc -l)
	rm *
	echo "$1 cleared"
		
	echo "$files files cleared"

	else
		echo "out_slurm does not exist"
		exit 999 
fi

}

fileclear "$@"
