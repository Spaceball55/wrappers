#!/bin/bash

# David Rauch
# email: david.rauch@bcm.edu
# Baylor College of Medicine MHG
# 6/13/2023

###

# fileclear.sh "$dir"
# Purpose: Clears a directory of all of its files. 

# inputs:
# "$dir" -> the directory you wish to clear
# outputs: N/A, clears te file out of the directory

# How to use:
# run the command with the directory you wish to clear as its argument (either relative or absolute path)
# ex:
# ./fileclear foo

# TROUBLESHOOTING
# Please make sure you only use 1 directory at a time
# The script does not access the files of the immediate working directory. 
#	If using relative paths, access the target directory from its parent directory.

function fileclear() {

ARGS=1 #we can only have 1 argument in this script

if [ $# -ne "$ARGS"  ]
then
	echo "Please only pass only one directory"
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
