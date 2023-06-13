#!/bin/bash

# David Rauch
# email: david.rauch@bcm.edu
# Baylor College of Medicine MHG
# 6/13/2023

###

# fileclear.sh "$dir"
# Purpose: Clears a directory of all of its files. Run this wrapper in the parent directory of the directory you wish to clear.
# inputs:
# "$dir" -> the directory you wish to clear
# outputs: N/A, clears te file out of the directory

# How to use:
# run the command with the directory you wish to clear as its argument (either relative or absolute path)
# ex:
# ./fileclear foo

# TROUBLESHOOTING:
# Please make sure you only use 1 directory at a time
# The script does not access the files of the immediate working directory. 
#	If using relative paths, access the target directory from its parent directory.

function fileclear() {

#check to make sure that the correct number of arguments are being passed
ARGS=1 #this function only allows for 1 argument
if [ $# -ne "$ARGS"  ]
then
	echo "Please only pass only one directory"
	exit 
fi

#check to see if the directory exists
if [ -d "$1" ]
then
	cd "$1"
	
	# if the directory is empty
	if [[ $(ls -A | wc -l) -eq 0 ]]
	then
		echo "$1 is already empty"
		exit 999
	fi
	
	numfiles=$(ls -l | wc -l) #counts the number of files in the directory
	rm *
	echo "$1 cleared"
		
	echo "$numfiles files cleared"

	else
		echo "$1 does not exist"
		exit 999 
fi
}

fileclear "$@"
